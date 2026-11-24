#!/usr/bin/env python3


"""
Demonstrate circular import failures inside a package.

This script imports the dark spellbook module directly and triggers a circular
dependency between dark spell modules.

Unlike the light implementation, the dark version intentionally keeps unsafe
imports to demonstrate how circular imports can break package initialization.
"""


from alchemy.grimoire.dark_spellbook import dark_spell_record


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def kaboom_1() -> None:
    """Trigger a circular import error with the dark spell modules."""
    # Attempt to record a dark spell through unsafe circular imports.
    spell = dark_spell_record(
        "Fantasy", "Earth, wind and fire")

    # These lines will never execute if the circular import fails.
    print(f"{C.BLUE}=== Kaboom 1 ==={C.RESET}")
    print(f"Access to {C.GREEN}'alchemy/grimoire/dark_spellbook.py'{C.RESET} "
          f"directly...\n Test import now - "
          f"{C.BG_RED}THIS WILL RAISE AN UNCAUGHT EXCEPTION{C.RESET}")
    print(f"{C.YELLOW}Testing record dark spell:{C.RESET} {spell}.")


if __name__ == "__main__":
    kaboom_1()
