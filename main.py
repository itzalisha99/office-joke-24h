"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to /output/entry.txt.
Python stdlib only, deterministic.
"""

import os

JOKE = (
    "The birthday card has been circulating for signatures since Tuesday, "
    "and the birthday was in March."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-200 chars, one line, not only whitespace."""
    if not text or text.strip() == "":
        raise ValueError("entry is empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
