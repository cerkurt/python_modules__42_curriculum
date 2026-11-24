#!/usr/bin/env python3


"""
Demonstrate nested imports through the alchemy potions module.

This script imports the `potions` module from the `alchemy` package and
accesses potion creation functions.

The potions module internally imports elemental functions from multiple modules
that demonstrating how modules can reuse distant code inside a package
structure.
"""


from alchemy import potions


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def distilation_0() -> None:
    """Test direct access to the alchemy potions module."""
    # Brew potions using functions exposed by the potions module.
    heal = potions.healing_potion()
    strength = potions.strength_potion()

    # Display the results of nested imports and potion creation.
    print(f"{C.BLUE}=== Distillation 0 ==={C.RESET}")
    print(f"Direct access to {C.GREEN}alchemy/potions.py{C.RESET}...")
    print(f"{C.YELLOW}Testing strength_potion:{C.RESET} {strength}.")
    print(f"{C.YELLOW}Testing healing_potion:{C.RESET} {heal}.\n")


if __name__ == "__main__":
    distilation_0()
