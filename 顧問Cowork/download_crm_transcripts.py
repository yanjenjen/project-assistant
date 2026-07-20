"""
CRM YouTube Transcript Downloader
Uses browser_cookie3 to read Chrome cookies → passes authenticated session to youtube-transcript-api
"""
import subprocess, sys, os, time

def pip_install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", pkg])

# Ensure dependencies
for pkg in ["youtube-transcript-api", "browser-cookie3", "requests"]:
    try:
        __import__(pkg.replace("-", "_"))
    except ImportError:
        print(f"Installing {pkg}...")
        pip_install(pkg)

import browser_cookie3
import requests
from youtube_transcript_api import YouTubeTranscriptApi

OUTPUT_DIR = r"C:\Users\jenny.lu\Documents\艾創點數位-ERP顧問\Odoo知識庫\工具\transcripts_crm"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Chrome cookies into a requests.Session
print("[INFO] Loading Chrome cookies...")
try:
    cookies = browser_cookie3.chrome(domain_name=".youtube.com")
    session = requests.Session()
    for c in cookies:
        session.cookies.set(c.name, c.value, domain=c.domain)
    print(f"[INFO] Loaded {len(session.cookies)} YouTube cookies from Chrome")
except Exception as e:
    print(f"[WARN] Could not load Chrome cookies: {e}")
    print("[WARN] Continuing without cookies (may fail)")
    session = None

VIDEOS = [
    ("CRM03", "eFe-yv_fkFI",  "CRM_Basics_Probabilities_and_Sales_Teams"),
    ("CRM04", "pPNuQNZzSLY",  "CRM_Scheduling_Activities"),
    ("CRM05", "FSG9fOkxxBM",  "Custom_Activities"),
    ("CRM06", "7QmhZrmA7SA",  "Activity_Plans"),
    ("CRM07", "u6kfb1oyneU",  "Won_and_Lost_Opportunities"),
    ("CRM08", "27UYtZJ9HKI",  "Sales_Teams_Setup_and_Leads_Assignment"),
    ("CRM09", "r9NEJ7fWfWQ",  "CRM_Activities_Automations_and_Reporting"),
    ("CRM10", "uypSO1MBMrw",  "Sales_Team_Reporting"),
    ("CRM11", "E6cAjrgHdJo",  "Gmail_Mailbox_Plugin"),
    ("CRM12", "SlO4C3EeG-4",  "Outlook_Mailbox_Plugin"),
    ("CRM13", "lKvueXqSNmQ",  "Marketing_Attribution_Report"),
    ("CRM14", "c0vTFtwZlVI",  "Scheduled_Activities_and_Moving_Opportunities"),
    ("CRM15", "B9ErlstQ1Ac",  "Partner_Autocomplete"),
    ("CRM16", "BSEf-EldDIA",  "CRM_Lead_and_Opportunity_Basics"),
    ("CRM17", "y3ZVeeM3WEc",  "Lead_Generation_Forms_and_Email_Aliases"),
    ("CRM18", "HFQ1c-VV3Qw",  "Lead_Generation_Events_Appointments_and_Website_Visitors"),
    ("CRM19", "GX_RyFvvxlY",  "Lead_Enrichment"),
    ("CRM20", "-nN9zMkI15s",  "Lead_Mining"),
    ("CRM21", "cSML0JkQ0Hg",  "Predictive_Lead_Scoring"),
    ("CRM22", "XL4-or5_T9Y",  "Gamification"),
]

ok, failed = [], []

for num, vid_id, title in VIDEOS:
    fname = os.path.join(OUTPUT_DIR, f"{num}_{title}.txt")
    if os.path.exists(fname):
        print(f"[SKIP] {num} already exists")
        ok.append(num)
        continue
    for attempt in range(3):
        try:
            # Pass the authenticated session as http_client
            api = YouTubeTranscriptApi(http_client=session) if session else YouTubeTranscriptApi()
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
                print(f"[RETRY] {num} attempt {attempt+1} failed ({e}), waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"[FAIL] {num} ({vid_id}): {e}")
                failed.append((num, str(e)))
    time.sleep(3)

print(f"\n=== Done: {len(ok)} OK, {len(failed)} failed ===")
if failed:
    for n, e in failed:
        print(f"  FAILED: {n} — {e}")
