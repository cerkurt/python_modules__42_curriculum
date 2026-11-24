#!/usr/bin/env python3


"""
Demonstrate direct access to a deeply nested package module.

This script imports `alchemy.transmutation.recipes` directly and uses the
recipe function responsible for lead transmutation.

The transmutation package demonstrates both absolute and relative imports
inside a nested package structure.
"""


import alchemy.transmutation.recipes


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def transmutation_0() -> None:
    """Test direct access to the transmutation recipes module."""
    # Create the lead-to-gold transmutation recipe.
    gold = alchemy.transmutation.recipes.lead_to_gold()

    # Display results produced through nested package imports.
    print(f"{C.BLUE}=== Transmutation 0 ==={C.RESET}")
    print(f"Using file {C.GREEN}'alchemy/transmutation/recipes.py'{C.RESET} "
          f"directly...")
    print(f"{C.YELLOW}Testing lead to gold:{C.RESET} {gold}.")


if __name__ == "__main__":
    transmutation_0()
