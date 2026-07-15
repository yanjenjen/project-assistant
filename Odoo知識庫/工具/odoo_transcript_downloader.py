#!/usr/bin/env python3
"""
Odoo 學習逐字稿批次下載工具
=====================================
使用方式：

【方式一】批次下載（推薦）
1. 在同一資料夾建立 urls.txt，每行貼一個 YouTube 網址
2. 執行：python3 odoo_transcript_downloader.py
3. 逐字稿自動存到 transcripts/ 資料夾

【方式二】單支下載
執行：python3 odoo_transcript_downloader.py "https://www.youtube.com/watch?v=xxxxx"

安裝需求：
pip install youtube-transcript-api
"""

from youtube_transcript_api import YouTubeTranscriptApi
import re
import os
import sys
from datetime import datetime


def extract_video_id(url):
    """從各種 YouTube 網址格式中提取 video ID"""
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com/shorts/([a-zA-Z0-9_-]{11})',
        r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
    ]
    url = url.strip()
    # 如果直接輸入 ID（11位字元）
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url):
        return url
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


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
        start = entry.start
        mins = int(start // 60)
        secs = int(start % 60)
        lines.append(f"[{mins:02d}:{secs:02d}] {entry.text}")

    return "\n".join(lines)


def get_transcript(video_id, prefer_lang='en'):
    """嘗試取得逐字稿，依語言優先順序"""
    api = YouTubeTranscriptApi()
    # 優先英文，再試中文，再試任意語言
    lang_orders = [
        [prefer_lang],
        ['en'],
        ['zh-TW', 'zh-CN', 'zh'],
        []  # 空列表 = 取第一個可用的
    ]
    for langs in lang_orders:
        try:
            if langs:
                return api.fetch(video_id, languages=langs)
            else:
                # 列出所有可用的，取第一個
                transcript_list = api.list(video_id)
                first = next(iter(transcript_list))
                return first.fetch()
        except Exception:
            continue
    raise Exception("找不到任何可用的逐字稿（影片可能未開放字幕）")


def download_transcript(url, output_dir="transcripts", index=None, total=None):
    """下載單支影片的逐字稿"""
    video_id = extract_video_id(url)
    prefix = f"[{index}/{total}] " if index and total else ""

    if not video_id:
        print(f"{prefix}❌ 無法解析網址: {url}")
        return False, None

    print(f"{prefix}正在下載: {video_id} ({url})")

    try:
        transcript = get_transcript(video_id)
        content = format_transcript(list(transcript), video_id, url)

        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{video_id}.txt")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        line_count = len(list(transcript))
        print(f"  ✅ 已儲存: {output_file}（{line_count} 段）")
        return True, output_file

    except Exception as e:
        print(f"  ❌ 下載失敗: {e}")
        # 建立錯誤紀錄
        error_file = os.path.join(output_dir, f"{video_id}_ERROR.txt")
        os.makedirs(output_dir, exist_ok=True)
        with open(error_file, 'w', encoding='utf-8') as f:
            f.write(f"影片 ID: {video_id}\n來源: {url}\n錯誤: {e}\n")
        return False, None


def main():
    # 判斷輸入方式
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        # 如果是 URL 或 video ID，直接下載單支
        if arg.startswith('http') or re.match(r'^[a-zA-Z0-9_-]{11}$', arg):
            print(f"\n下載單支影片逐字稿...\n")
            download_transcript(arg, output_dir="transcripts")
            return
        # 否則當作 urls 檔案路徑
        urls_file = arg
    else:
        urls_file = os.path.join(os.path.dirname(__file__), "urls.txt")

    # 讀取 URLs 清單
    if not os.path.exists(urls_file):
        print(f"找不到 {urls_file}")
        print("請建立 urls.txt，每行一個 YouTube 網址，再重新執行。")
        print("\n範例 urls.txt 內容：")
        print("https://www.youtube.com/watch?v=NoxYrnnHgfk")
        print("https://www.youtube.com/watch?v=xxxxxxxxxxxxxxxx")
        return

    with open(urls_file, 'r', encoding='utf-8') as f:
        urls = [
            line.strip() for line in f
            if line.strip() and not line.strip().startswith('#')
        ]

    if not urls:
        print("urls.txt 是空的，請填入 YouTube 網址後再執行。")
        return

    # 建立輸出資料夾（以執行時間命名）
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    output_dir = os.path.join(os.path.dirname(__file__), f"transcripts_{timestamp}")

    print(f"\n{'='*60}")
    print(f"  Odoo 逐字稿批次下載")
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

    # 產出摘要
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
