#!/usr/bin/env python3

"""
Demonstrate importing specific functions with the from-import syntax.

This script imports the `create_water` function directly from `elements.py`
using the `from ... import ...` structure.

This import style allows direct access to imported objects without using the
module namespace.
"""


from elements import create_water


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def alembic_1() -> None:
    """Test direct function import from the local elements module."""
    water = create_water()
    print(f"{C.BLUE}=== Alembic 1 ==={C.RESET}")
    print(f"Using: {C.GREEN}'from ... import ...'{C.RESET} structure to "
          f"access {C.GREEN}elements.py{C.RESET}.")
    print(f"{C.YELLOW}Testing create_water:{C.RESET} {water}.\n")


if __name__ == "__main__":
    alembic_1()
