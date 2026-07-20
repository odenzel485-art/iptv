#!/usr/bin/env python3
"""
YouTube to IPTV - Multi Channel Builder
Uses cookies.txt file exported from your browser.
"""

import subprocess
import sys
import time
import os

COOKIES_FILE = "cookies.txt"

def get_stream_url(youtube_url):
    """Get stream URL using cookies.txt."""
    
    if not os.path.isfile(COOKIES_FILE):
        print(f"\n    ❌ '{COOKIES_FILE}' not found in the current folder.")
        print("    → Export cookies from Chrome using the extension.")
        print("    → Save the file as 'cookies.txt' in this folder.")
        return None
    
    try:
        cmd = [
            "python", "-m", "yt_dlp",
            "-g",
            "--no-check-certificate",
            "--cookies", COOKIES_FILE,
            "--throttled-rate", "1000000",
            youtube_url
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        return lines[0] if lines else None
    except subprocess.CalledProcessError as e:
        print(f"\n    ❌ Error:\n{e.stderr.strip()}\n")
        return None

def main():
    print("=" * 50)
    print("🎬 YouTube to IPTV - Multi Channel Builder")
    print("=" * 50)
    print("\nMake sure 'cookies.txt' is in the current folder.")
    print("Type 'done' as the channel name when finished.\n")

    # Check if cookies file exists
    if os.path.isfile(COOKIES_FILE):
        print(f"✅ Found {COOKIES_FILE} – good to go!\n")
    else:
        print(f"❌ {COOKIES_FILE} not found.")
        print("   Please export cookies from Chrome and save as 'cookies.txt' in this folder.\n")

    channels = []
    while True:
        name = input("Channel name (e.g., Citizen TV): ").strip()
        if name.lower() == "done":
            break
        url = input("YouTube URL (paste the full link): ").strip()
        if url:
            channels.append((name, url))
        print()

    if not channels:
        print("❌ No channels added.")
        return

    print(f"\n📥 Fetching stream URLs for {len(channels)} channel(s)...\n")
    m3u_lines = ["#EXTM3U"]

    for name, url in channels:
        print(f"  ⏳ {name} ... ", end="", flush=True)
        stream = get_stream_url(url)
        if stream:
            m3u_lines.append(f'#EXTINF:-1,{name}')
            m3u_lines.append(stream)
            print("✅ Done")
        else:
            print("❌ Failed")
        time.sleep(1)

    output_file = "kenya_iptv.m3u"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(m3u_lines))

    print(f"\n✅ Playlist saved as: {output_file}")
    print("📺 Open this file in VLC, TiviMate, or any IPTV player.")

if __name__ == "__main__":
    main()