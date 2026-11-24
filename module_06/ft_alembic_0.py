#!/usr/bin/env python3

"""
Demonstrate importing from a local module with absolute imports.

This script imports the local `elements.py` module using the standard
`import module` syntax and accesses functions through the module namespace.

Absolute imports use the complete module or package path and help keep imports
explicit and readable.
"""


import elements


class C:
    """Store ANSI escape codes used for colored terminal output."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def alembic_0() -> None:
    """Test access to the local elements module."""
    fire = elements.create_fire()
    print(f"{C.BLUE}=== Alembic 0 ==={C.RESET}")
    print(f"Using: {C.GREEN}'import ...'{C.RESET} structure to access "
          f"{C.GREEN}elements.py{C.RESET}.")
    print(f"{C.YELLOW}Testing create_fire:{C.RESET} {fire}.\n")


if __name__ == "__main__":
    alembic_0()
