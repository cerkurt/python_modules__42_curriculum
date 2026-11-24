#!/usr/bin/env python3


"""
Demonstrate avoiding circular imports inside a package.

This script imports the `grimoire` package and records a light spell using the
light spellbook module.

The light magic implementation avoids circular dependencies by carefully
organizing imports between modules.
"""


import alchemy.grimoire


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def kaboom_0() -> None:
    """Test successful spell recording without circular imports."""
    # Record a light spell through the grimoire package.
    spell = alchemy.grimoire.light_spellbook.light_spell_record(
        "Fantasy", "Earth, wind and fire")

    # Display the result of safe package imports and validation.
    print(f"{C.BLUE}=== Kaboom 0 ==={C.RESET}")
    print(f"Using {C.GREEN}'grimoire module'{C.RESET} only...")
    print(f"{C.YELLOW}Testing record light spell:{C.RESET} {spell}.")


if __name__ == "__main__":
    kaboom_0()
