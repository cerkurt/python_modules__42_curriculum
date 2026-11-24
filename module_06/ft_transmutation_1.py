#!/usr/bin/env python3


"""
Demonstrate importing a package module through its namespace.

This script imports the `transmutation` module from the `alchemy` package and
accesses recipe functions through the module namespace.

Using module namespaces helps organize related functionality and makes package
hierarchies easier to understand.
"""


import alchemy.transmutation


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def transmutation_1() -> None:
    """Test access to the transmutation module through alchemy."""
    # Access the recipe module through the transmutation package.
    gold = alchemy.transmutation.recipes.lead_to_gold()

    # Display the result of the lead transmutation recipe.
    print(f"{C.BLUE}=== Transmutation 1 ==={C.RESET}")
    print(f"Import {C.GREEN}'transmutation module'{C.RESET} directly...")
    print(f"{C.YELLOW}Testing lead to gold:{C.RESET} {gold}.")


if __name__ == "__main__":
    transmutation_1()
