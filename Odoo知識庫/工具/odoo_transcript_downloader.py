#!/usr/bin/env python3
"""
Odoo 學習逐字稿批次下載工具
=====================================
使用方式：

【方式一】批次下載（推薦）
1. 在同一資料夾建立 urls.txt，每行貼一個 YouTube 網址
2. 執行：python odoo_transcript_downloader.py urls_inventory.txt
3. 逐字稿自動存到 transcripts_YYYYMMDD_HHMM/ 資料夾

【方式二】單支下載
執行：python odoo_transcript_downloader.py "https://www.youtube.com/watch?v=xxxxx"

安裝需求：
pip install yt-dlp
"""

import yt_dlp
import json
import os
import re
import sys
import tempfile
from datetime import datetime

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def extract_video_id(url):
    """從各種 YouTube 網址格式中提取 video ID"""
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com/shorts/([a-zA-Z0-9_-]{11})',
        r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
    ]
    url = url.strip()
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url):
        return url
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def parse_json3(content):
    """解析 json3 格式字幕，回傳 [{'start': float, 'text': str}]"""
    data = json.loads(content)
    entries = []
    for event in data.get('events', []):
        if 'segs' not in event:
            continue
        start = event.get('tStartMs', 0) / 1000.0
        text = ''.join(seg.get('utf8', '') for seg in event['segs']).strip()
        if text and text != '\n':
            entries.append({'start': start, 'text': text})
    return entries


def parse_vtt(content):
    """解析 WebVTT 格式字幕"""
    entries = []
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if '-->' in line:
            time_match = re.match(r'(\d{2}):(\d{2}):(\d{2})\.(\d{3})', line)
            if not time_match:
                # mm:ss.mmm 格式
                time_match = re.match(r'(\d{2}):(\d{2})\.(\d{3})', line)
                if time_match:
                    m, s, ms = map(int, time_match.groups())
                    start = m * 60 + s + ms / 1000.0
                else:
                    i += 1
                    continue
            else:
                h, m, s, ms = map(int, time_match.groups())
                start = h * 3600 + m * 60 + s + ms / 1000.0
            i += 1
            text_lines = []
            while i < len(lines) and lines[i].strip():
                text_lines.append(lines[i].strip())
                i += 1
            text = ' '.join(text_lines)
            text = re.sub(r'<[^>]+>', '', text).strip()
            if text:
                entries.append({'start': start, 'text': text})
        else:
            i += 1
    return entries


def get_transcript(video_id):
    """使用 yt-dlp 下載字幕，回傳 [{'start': float, 'text': str}]"""
    url = f"https://www.youtube.com/watch?v={video_id}"

    with tempfile.TemporaryDirectory() as tmpdir:
        ydl_opts = {
            'skip_download': True,
            'writeautomaticsub': True,
            'writesubtitles': True,
            'subtitleslangs': ['en', 'en-orig', 'en-US'],
            'subtitlesformat': 'json3/vtt/best',
            'outtmpl': os.path.join(tmpdir, '%(id)s'),
            'quiet': True,
            'no_warnings': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # 尋找下載的字幕檔
        sub_file = None
        for fname in os.listdir(tmpdir):
            if fname.endswith('.json3') or fname.endswith('.vtt'):
                sub_file = os.path.join(tmpdir, fname)
                break

        if not sub_file:
            raise Exception("找不到任何可用的字幕（影片可能未開放字幕）")

        with open(sub_file, 'r', encoding='utf-8') as f:
            content = f.read()

        if sub_file.endswith('.json3'):
            return parse_json3(content)
        else:
            return parse_vtt(content)


def format_transcript(entries, video_id, url=""):
    """格式化逐字稿，加入時間戳與說明"""
    lines = []
    lines.append(f"影片 ID: {video_id}")
    if url:
        lines.append(f"來源: {url}")
    lines.append(f"下載時間: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 60)
    lines.append("")

    for entry in entries:
        start = entry['start']
        mins = int(start // 60)
        secs = int(start % 60)
        lines.append(f"[{mins:02d}:{secs:02d}] {entry['text']}")

    return "\n".join(lines)


def download_transcript(url, output_dir="transcripts", index=None, total=None):
    """下載單支影片的逐字稿"""
    video_id = extract_video_id(url)
    prefix = f"[{index}/{total}] " if index and total else ""

    if not video_id:
        print(f"{prefix}❌ 無法解析網址: {url}")
        return False, None

    print(f"{prefix}正在下載: {video_id} ({url})")

    try:
        entries = get_transcript(video_id)
        content = format_transcript(entries, video_id, url)

        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{video_id}.txt")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✅ 已儲存: {output_file}（{len(entries)} 段）")
        return True, output_file

    except Exception as e:
        print(f"  ❌ 下載失敗: {e}")
        error_file = os.path.join(output_dir, f"{video_id}_ERROR.txt")
        os.makedirs(output_dir, exist_ok=True)
        with open(error_file, 'w', encoding='utf-8') as f:
            f.write(f"影片 ID: {video_id}\n來源: {url}\n錯誤: {e}\n")
        return False, None


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.startswith('http') or re.match(r'^[a-zA-Z0-9_-]{11}$', arg):
            print(f"\n下載單支影片逐字稿...\n")
            download_transcript(arg, output_dir="transcripts")
            return
        urls_file = arg
    else:
        urls_file = os.path.join(os.path.dirname(__file__), "urls.txt")

    if not os.path.exists(urls_file):
        print(f"找不到 {urls_file}")
        print("請建立 urls.txt，每行一個 YouTube 網址，再重新執行。")
        return

    with open(urls_file, 'r', encoding='utf-8') as f:
        urls = [
            line.strip() for line in f
            if line.strip() and not line.strip().startswith('#')
        ]

    if not urls:
        print("urls.txt 是空的，請填入 YouTube 網址後再執行。")
        return

    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    output_dir = os.path.join(os.path.dirname(__file__), f"transcripts_{timestamp}")

    print(f"\n{'='*60}")
    print(f"  Odoo 逐字稿批次下載（yt-dlp 版）")
    print(f"  共 {len(urls)} 支影片 → {output_dir}")
    print(f"{'='*60}\n")

    success_files = []
    fail_count = 0

    for i, url in enumerate(urls, 1):
        ok, filepath = download_transcript(url, output_dir=output_dir, index=i, total=len(urls))
        if ok:
            success_files.append(filepath)
        else:
            fail_count += 1
        print()

    print(f"{'='*60}")
    print(f"  完成！成功：{len(success_files)}／{len(urls)}  失敗：{fail_count}")
    print(f"  輸出資料夾：{output_dir}")
    print(f"{'='*60}")

    if success_files:
        print("\n已下載的逐字稿：")
        for f in success_files:
            print(f"  - {os.path.basename(f)}")


if __name__ == "__main__":
    main()
