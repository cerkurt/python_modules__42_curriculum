#!/usr/bin/env python3


"""
Demonstrate package initialization through the alchemy module.

This script imports the `alchemy` package directly and accesses objects exposed
through its `__init__.py` file.

The package interface only exposes selected functions. Functions not exported
by `__init__.py` cannot be accessed directly through the package namespace.
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


def alembic_4() -> None:
    """Test package-level access through the alchemy interface."""
    air = alchemy.create_air()
    print(f"{C.BLUE}=== Alembic 4 ==={C.RESET}")
    print(f"Accessing the {C.GREEN}alchemy module{C.RESET} using "
          f"{C.GREEN}'import alchemy'{C.RESET}.")
    print(f"{C.YELLOW}Testing create_air:{C.RESET} {air}.\n")
    print(f"Now show that not all functions can be reached...\n"
          f"{C.BG_RED}This will raise an exception!{C.RESET}")
    print(f"{C.YELLOW}Testing the hidden create_earth:{C.RESET}", end=" ")
    print(f"{alchemy.create_earth()}")


if __name__ == "__main__":
    alembic_4()
