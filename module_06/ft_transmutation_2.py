#!/usr/bin/env python3


"""
Demonstrate package-level access through the alchemy module.

This script imports the `alchemy` package directly and accesses transmutation
functions exposed through nested package modules.

The example demonstrates how package initialization can expose complex internal
structures through a simplified interface.
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


def transmutation_2() -> None:
    """Test transmutation access through the alchemy package."""
    # Access the transmutation recipe through the alchemy package.
    gold = alchemy.transmutation.recipes.lead_to_gold()
    # Display the result of package-level transmutation access.
    print(f"{C.BLUE}=== Transmutation 2 ==={C.RESET}")
    print(f"Import {C.GREEN}'alchemy module'{C.RESET} only...")
    print(f"{C.YELLOW}Testing lead to gold:{C.RESET} {gold}.")


if __name__ == "__main__":
    transmutation_2()
