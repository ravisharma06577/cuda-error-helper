"""Tiny CLI: describe your CUDA error, get the matching troubleshooting guide."""
import sys
from pathlib import Path

GUIDES_DIR = Path(__file__).parent.parent / "guides"

KEYWORDS = {
    "nvcc-not-found.md": ["nvcc", "not found", "command not found", "path"],
    "driver-version-insufficient.md": ["driver", "insufficient", "version", "runtime version"],
    "no-cuda-capable-device.md": ["no cuda-capable", "capable device", "no_device", "cuinit", "no gpu", "not detected"],
    "cuda-install-failed.md": ["install", "installer", "installation", "failed"],
}


def title_of(path):
    return path.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()


def list_guides():
    print("Available guides:\n")
    for name in sorted(KEYWORDS):
        p = GUIDES_DIR / name
        if p.exists():
            print(f"  - {title_of(p)}")


def best_match(query):
    q = query.lower()
    scores = {name: sum(k in q for k in kws) for name, kws in KEYWORDS.items()}
    name, score = max(scores.items(), key=lambda x: x[1])
    return name if score > 0 else None


def main():
    args = sys.argv[1:]
    if not args or args[0] == "--list":
        list_guides()
        print('\nUsage: python3 src/fix.py "your error message"')
        return
    match = best_match(" ".join(args))
    if match is None:
        print("No matching guide found.\n")
        list_guides()
        return
    print((GUIDES_DIR / match).read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
