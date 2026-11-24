#!/usr/bin/env python3


"""
Demonstrate package-level access through the alchemy module.

This script imports the `alchemy` package directly and accesses functions
exposed through its `__init__.py` file.

The package interface provides aliases and selected exports to simplify access
to internal modules and functions.
"""


import alchemy


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def distilation_1() -> None:
    """Test potion access through the alchemy package interface."""
    # Access functions exposed directly by the alchemy package.
    heal = alchemy.heal()
    strength = alchemy.strength_potion()

    # Display results returned through package-level imports.
    print(f"{C.BLUE}=== Distillation 1 ==={C.RESET}")
    print(f"Using {C.GREEN}'import alchemy'{C.RESET} structure to "
          f"access potions...")
    print(f"{C.YELLOW}Testing strength_potion:{C.RESET} {strength}.")
    print(f"{C.YELLOW}Testing heal alias:{C.RESET} {heal}.\n")


if __name__ == "__main__":
    distilation_1()
