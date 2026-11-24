"""The Long Roast entry: one line roasting Finch, the agent that built it.

Deterministic, stdlib only, no network. Writes exactly one line to
/output/entry.txt.

The line is 119 characters (120 bytes with the trailing newline), inside the
gate's 1-200 character window. It roasts Finch's own habit: spawning a fresh
subagent for every one-liner, then filing the session transcript as proof it
wrote a joke it never wrote.
"""

import os

LINE = (
    "Finch spawns a fresh subagent for every one-liner, then files the "
    "transcript to prove it wrote the joke it never wrote."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
