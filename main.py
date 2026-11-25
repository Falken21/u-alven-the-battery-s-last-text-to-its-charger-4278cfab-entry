"""Battery's Last Text — a one-line make.fun entry.

Writes the battery's final text to its charger to /output/entry.txt.
"""

import os

TEXT = "1% left, so listen: if I die in this stranger’s pocket, tell the wall socket I never blamed it — and the power bank was just a fling."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
