#!/usr/bin/env python3

from enum import Enum
import sys
import os


class C(str, Enum):
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"

    def __str__(self) -> str:
        return self.value


def command_quest() -> None:
    prog_name = os.path.basename(sys.argv[0])

    if len(sys.argv) == 1:
        print(f"No arguments provided!\n"
              f"{C.YELLOW}Program Name:{C.RESET} {prog_name}\n"
              f"{C.YELLOW}Total Arguments:{C.RESET} {len(sys.argv)}")

    else:
        print(f"{C.YELLOW}Program Name:{C.RESET} {prog_name}\n"
              f"{C.YELLOW}Arguments Received:{C.RESET} {len(sys.argv) - 1}")
        n = 1
        while n < len(sys.argv):
            print(f"{C.YELLOW}Argument {n}:{C.RESET} {sys.argv[n]}")
            n += 1
        print(f"{C.YELLOW}Total Arguments:{C.RESET} {len(sys.argv)}")


def main() -> None:
    print(f"{C.BLUE}=== Command Quest ==={C.RESET}")
    command_quest()


if __name__ == "__main__":
    main()
