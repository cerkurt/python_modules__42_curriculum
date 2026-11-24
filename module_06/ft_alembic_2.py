#!/usr/bin/env python3

"""
Demonstrate importing from a package module using absolute imports.

This script imports the `alchemy.elements` module using the standard
`import package.module` syntax.

Absolute imports use the complete package path and make it clear where imported
objects come from.
"""


import alchemy.elements


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def alembic_2() -> None:
    """Test access to a module inside the alchemy package."""
    earth = alchemy.elements.create_earth()
    print(f"{C.BLUE}=== Alembic 2 ==={C.RESET}")
    print(f"Accessing {C.GREEN}alchemy/elements.py{C.RESET} using "
          f"{C.GREEN}'import ...'{C.RESET} structure.")
    print(f"{C.YELLOW}Testing create_earth:{C.RESET} {earth}.\n")


if __name__ == "__main__":
    alembic_2()
