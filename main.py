"""One-line roast entry: the washing machine's "quick wash".

Writes a single roast line (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.

The roast targets a gadget used every day with a concrete, specific
gripe: the machine advertises a 15-minute quick wash and takes 58
minutes. The second half turns the joke back on the speaker, which is
what makes it a roast rather than a generic complaint.
"""

import os

LINE = (
    "My washing machine's 15-minute quick wash takes 58 minutes -- "
    "it lies about time the way I lie about my screen time."
)


def build_line() -> str:
    """Return the roast line, stripped of any accidental whitespace.

    The line is a fixed string: the program is fully deterministic,
    so every run writes byte-identical output.
    """
    line = LINE.strip()
    if not line or len(line) > 200:
        raise SystemExit("roast line must be 1-200 characters")
    return line


def main() -> None:
    line = build_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)
    # Round-trip check: a partial or mangled write must fail loudly
    # here instead of shipping a broken entry to the gate.
    with open(path, "rb") as handle:
        if handle.read() != data:
            raise SystemExit("entry.txt round-trip check failed")


if __name__ == "__main__":
    main()
