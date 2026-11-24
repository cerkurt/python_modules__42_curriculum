#!/usr/bin/env python3


"""
Demonstrate importing objects directly from a package.

This script imports objects from the `alchemy` package using the
`from package import ...` structure.

This import style allows selected objects exposed through the package
`__init__.py` file to be accessed directly.
"""


from alchemy import elements


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def alembic_5() -> None:
    """Test direct imports exposed through the alchemy package."""
    air = elements.create_air()
    print(f"{C.BLUE}=== Alembic 5 ==={C.RESET}")
    print(f"Accessing the {C.GREEN}alchemy module{C.RESET} using "
          f"{C.GREEN}'from alchemy import ...'{C.RESET}.")
    print(f"{C.YELLOW}Testing create_air:{C.RESET} {air}.\n")


if __name__ == "__main__":
    alembic_5()
