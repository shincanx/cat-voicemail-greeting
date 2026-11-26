#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — writes one cat voicemail line to entry.txt."""

import os

LINE = "Hi, it's Mittens. I'm napping in the box you threw out. Leave a message \u2014 or better, open the tuna. Beep."


def main():
    if not 1 <= len(LINE) <= 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
