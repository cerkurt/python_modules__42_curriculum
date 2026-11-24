#!/usr/bin/env python3

"""
Demonstrate importing from a package using the from-import syntax.

This script imports the `elements` module from the `alchemy` package using the
`from ... import ...` structure.

This import style allows direct access to package modules while keeping the
package hierarchy explicit.
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


def alembic_3() -> None:
    """Test importing a module from the alchemy package."""
    air = elements.create_air()
    print(f"{C.BLUE}=== Alembic 3 ==={C.RESET}")
    print(f"Accessing {C.GREEN}alchemy/elements.py{C.RESET} using "
          f"{C.GREEN}'from ... import ...'{C.RESET} structure.")
    print(f"{C.YELLOW}Testing create_air:{C.RESET} {air}.\n")


if __name__ == "__main__":
    alembic_3()
