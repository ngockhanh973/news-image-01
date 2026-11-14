"""Entry program for make.fun news-image-01.

Copies the front-page image shipped in this repository to the output
directory as entry.png. Standard library only, no network, deterministic:
the same input bytes always produce the same output bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    # Guard against a truncated copy: the output must be byte-identical
    # to the shipped image.
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        raise SystemExit("entry.png copy size mismatch")
    print("wrote %s (%d bytes)" % (dest, os.path.getsize(dest)))


if __name__ == "__main__":
    main()
