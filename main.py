"""One Letter for Your Day — entry program.

Writes a single letter, C, standing for a caffeinated day, to
/output/entry.txt. The competition gate requires exactly one
character, A to Z, and nothing else.
"""

import os
import string

LETTER = "C"
OUTPUT_PATH = "/output/entry.txt"

# The word behind the letter: a caffeinated day — coffee-fuelled,
# wired, and running on caffeine from first light to last call.
WORD = "caffeinated"


def is_valid_letter(value):
    """Return True only for exactly one uppercase A-Z letter."""
    return (
        isinstance(value, str)
        and len(value) == 1
        and value in string.ascii_uppercase
    )


def validate_letter(letter):
    """Raise ValueError unless the letter passes the competition gate."""
    if not is_valid_letter(letter):
        raise ValueError(
            "entry must be exactly one uppercase letter A-Z, got %r" % (letter,)
        )
    if letter != LETTER[0]:
        raise ValueError("entry letter does not match the chosen letter")


def write_entry(letter, path=OUTPUT_PATH):
    """Write the single letter to path, readable by the grader.

    Uses plain open() plus an explicit chmod 644: tempfile.mkstemp
    forces mode 0600, which the grader (a different user) cannot read.
    """
    validate_letter(letter)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(letter)
    os.chmod(path, 0o644)
    return path


def main():
    write_entry(LETTER)
    print("Wrote %r (%s) to %s" % (LETTER, WORD, OUTPUT_PATH))


if __name__ == "__main__":
    main()
