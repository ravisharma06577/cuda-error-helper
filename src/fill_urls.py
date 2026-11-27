"""Helper: asks for the URL of each thread that is missing one."""
import csv
from pathlib import Path

PATH = Path(__file__).parent.parent / "data" / "threads.csv"
PREFIX = "https://forums.developer.nvidia.com/"

with open(PATH, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

missing = [r for r in rows if not (r["url"] or "").strip()]
print(f"{len(missing)} threads are missing a URL. Press Enter to skip one, Ctrl+C to stop (progress is saved).\n")

try:
    for r in missing:
        print(f"Title: {r['title']}")
        url = input("URL: ").strip()
        if url.startswith(PREFIX):
            r["url"] = url
        elif url:
            print("  Skipped: link must start with", PREFIX)
        print()
except KeyboardInterrupt:
    print("\nStopped.")

with open(PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["title", "url"])
    w.writeheader()
    w.writerows(rows)

left = sum(1 for r in rows if not (r["url"] or "").strip())
print(f"Saved. Still missing: {left}")
