"""
CRM20-22 Transcript Fetcher
Uses Netscape cookie file (exported by "Get cookies.txt LOCALLY" extension)
No browser_cookie3 needed — uses standard http.cookiejar instead
"""
import http.cookiejar, requests, os, time
from youtube_transcript_api import YouTubeTranscriptApi

# ── SETTINGS ──────────────────────────────────────────────────────────────
COOKIE_FILE = r"C:\Users\jenny.lu\Downloads\Lead Mining.txt"
OUTPUT_DIR  = r"C:\Users\jenny.lu\Documents\艾創點數位-ERP顧問\Odoo知識庫\工具\transcripts_crm"
# ──────────────────────────────────────────────────────────────────────────

VIDEOS = [
    ("CRM20", "-nN9zMkI15s", "Lead_Mining"),
    ("CRM21", "cSML0JkQ0Hg", "Predictive_Lead_Scoring"),
    ("CRM22", "XL4-or5_T9Y", "Gamification"),
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Netscape cookie file with standard library (no browser_cookie3 needed)
print(f"[INFO] Loading cookies from: {COOKIE_FILE}")
jar = http.cookiejar.MozillaCookieJar(COOKIE_FILE)
jar.load(ignore_discard=True, ignore_expires=True)
session = requests.Session()
session.cookies = jar
print(f"[INFO] Loaded {len(list(jar))} cookies")

api = YouTubeTranscriptApi(http_client=session)

ok, failed = [], []
for num, vid_id, title in VIDEOS:
    fname = os.path.join(OUTPUT_DIR, f"{num}_{title}.txt")
    if os.path.exists(fname):
        print(f"[SKIP] {num} already exists")
        ok.append(num)
        continue
    for attempt in range(3):
        try:
            transcript = api.fetch(vid_id, languages=["en"])
            text = " ".join(
                seg.text.strip() for seg in transcript
                if seg.text.strip() and seg.text.strip().lower() != "[music]"
            )
            with open(fname, "w", encoding="utf-8") as f:
                f.write(f"# {num}: {title.replace('_', ' ')}\n")
                f.write(f"# Video ID: {vid_id}\n")
                f.write(f"# Source: https://www.youtube.com/watch?v={vid_id}\n\n")
                f.write(text)
            print(f"[OK] {num} — {len(text)} chars saved")
            ok.append(num)
            break
        except Exception as e:
            if attempt < 2:
                wait = 15 * (attempt + 1)
                print(f"[RETRY] {num} attempt {attempt+1} failed: {e} — waiting {wait}s")
                time.sleep(wait)
            else:
                print(f"[FAIL] {num} ({vid_id}): {e}")
                failed.append((num, str(e)))
    time.sleep(3)

print(f"\n=== Done: {len(ok)} OK, {len(failed)} failed ===")
for n, e in failed:
    print(f"  FAILED: {n} — {e}")
