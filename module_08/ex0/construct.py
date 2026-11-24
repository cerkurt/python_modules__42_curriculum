#!/usr/bin/env python3


"""
Check whether Python is running inside a virtual environment.

This script compares the active Python environment with the base Python
installation. If both paths are the same, the script is running in the global
environment. If they are different, a virtual environment is active.

The goal is to show why virtual environments are useful: they isolate installed
packages and keep the global Python installation clean.
"""


# The sys module gives information about the Python interpreter currently used.
import sys
# The site module gives access to Python package installation directories.
import site
import os


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


def construct() -> None:
    """Print information about the current Python environment.

    sys.prefix points to the active Python environment.
    sys.base_prefix points to the original base Python installation.

    When both values are equal, no virtual environment is active.
    When they are different, Python is running inside a virtual environment.
    """

    # Active environment path. In a venv, this points to the venv folder.
    env_1 = sys.prefix
    # Base Python path. Points to the original Python installation.
    env_2 = sys.base_prefix

    # If both paths are the same, Python IS NOT running inside a venv.
    if env_1 == env_2:
        pass
    else:
        # Extract only the folder name of the active virtual environment.
        venv_name = os.path.basename(sys.prefix)

    # Commands shown to the user for activating the virtual environment.
    unix = "source matrix_env/bin/activate"
    windows = "matrix_env\\Scripts\\activate"

    # First output branch: no virtual environment was detected.
    if env_1 == env_2:
        print(f"{C.BLUE}\nMATRIX STATUS:{C.RESET} You're still plugged in\n\n"
              f"{C.YELLOW}Current Python:{C.RESET} {env_1}\n"
              f"{C.YELLOW}Virtual Environment:{C.RESET} "
              f"{venv_name} detected\n")

        print(f"{C.BG_RED}WARNING:{C.RESET} You're in the global "
              f"environment!\nThe machines can see everything you install.\n\n"
              f"To enter the construct, run:\n"
              f"{C.YELLOW}python-m venv matrix_env{C.RESET}\n"
              f"{C.PURPLE}{unix}{C.RESET} # On Unix\n"
              f"{C.PURPLE}{windows}{C.RESET} # On Windows\n"
              f"\nThen run this program again.")

    # Second output branch: a virtual environment was detected.
    else:
        print(f"{C.BLUE}\nMATRIX STATUS:{C.RESET} Welcome to the construct\n\n"
              f"{C.YELLOW}Current Python:{C.RESET} {env_1}\n"
              f"{C.YELLOW}Virtual Environment:{C.RESET} "
              f"{venv_name} detected\n"
              f"{C.YELLOW}Environmental Path:{C.RESET}{sys.prefix}\n")

        print(f"{C.GREEN}SUCCESS:{C.RESET} You're in an isolated "
              f"environment!\nSafe to install packages without affecting the "
              f"global system.\n\n{C.YELLOW}Package installation path: "
              f"{C.RESET}{site.getsitepackages()[0]}")


if __name__ == "__main__":
    construct()
