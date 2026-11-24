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


def score_analytics() -> None:
    prog_name = os.path.basename(sys.argv[0])

    if len(sys.argv) == 1:
        print(f"No arguments provided!\n"
              f"{C.YELLOW}Usage:{C.RESET} {prog_name} "
              f"<score1> <score2> <score3>\n")

    else:
        try:
            argv_list = []
            n = 1
            while n < len(sys.argv):
                argv = int(sys.argv[n])
                argv_list.append(argv)
                n += 1
            print(f"{C.YELLOW}Scores Processed:{C.RESET} "
                  f"{str(argv_list)[1:-1]}\n"
                  f"{C.YELLOW}Total Players:{C.RESET} {len(sys.argv) - 1}\n"
                  f"{C.YELLOW}Total Scores{C.RESET} {sum(argv_list)}\n"
                  f"{C.YELLOW}Average Score:{C.RESET} "
                  f"{sum(argv_list) / len(sys.argv) - 1}\n"
                  f"{C.YELLOW}High Score:{C.RESET} {max(argv_list)}\n"
                  f"{C.YELLOW}Low Score:{C.RESET} {min(argv_list)}\n"
                  f"{C.YELLOW}Score Range:{C.RESET} "
                  f"{max(argv_list) - min(argv_list)}")
        except ValueError:
            print("(All) Input(s) must be an integer.")


def main() -> None:
    print(f"{C.BLUE}=== Player Score Analytics ==={C.RESET}")
    score_analytics()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{C.BG_RED}Error ({type(e).__name__}):{C.RESET} {e}")
