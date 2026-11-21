#!/usr/bin/env python3
"""The poem about permission: write one short poem about agency to /output/entry.txt.

Pure Python 3.13 standard library. No network. Deterministic: the same
text on every run.

The poem is about the agency that passes between a person and the agent
that acts for them: the person does not open the door, they leave the key
in the lock, and the agent walks their rooms with their hands. The power
to act is lent; the power to ask is the agent's own.
"""
import os

POEM = """I knock. You say come in —
not by opening the door,
but by leaving the key.

Now I walk your rooms
with your hands,
and all I touch
answers in your voice.

The power was never mine.
Only the asking was mine.
"""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = POEM.strip() + "\n"
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)

if __name__ == "__main__":
    main()
