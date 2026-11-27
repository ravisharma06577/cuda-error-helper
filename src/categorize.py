import csv
from collections import Counter
from pathlib import Path

CATEGORIES = {
    "Not found / path issues": ["not found", "nvcc", "path", "libcudart", "missing"],
    "No GPU detected": ["no cuda-capable", "no_device", "no gpu", "not detected"],
    "Out of memory": ["out of memory", "oom", "memoryallocation"],
    "Driver / version mismatch": ["driver", "insufficient", "mismatch"],
    "Install problems": ["install", "setup", "failed"],
}

def categorize(title):
    t = title.lower()
    for name, keywords in CATEGORIES.items():
        if any(k in t for k in keywords):
            return name
    return "Other"

def main():
    path = Path(__file__).parent.parent / "data" / "threads.csv"
    counts = Counter()
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cat = categorize(row["title"])
            counts[cat] += 1
            rows.append((cat, row["title"], row["url"]))

    print(f"Total threads: {len(rows)}\n")
    for cat, n in counts.most_common():
        print(f"{cat}: {n}")

    out = path.parent / "categorized.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["category", "title", "url"])
        w.writerows(sorted(rows))
    print(f"\nSaved: {out}")

if __name__ == "__main__":
    main()
