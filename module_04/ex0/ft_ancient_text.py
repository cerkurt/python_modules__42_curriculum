#!/usr/bin/env python3

"""Read a file from the command line and display its contents safely."""

import sys


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def ancient_text() -> None:
    """Read a file given in the command line and display its contents."""

    # Initialize file handler to safely manage it in finally block.
    file_to_read = None

    # Ensure exactly one filename argument is provided.
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    # Retrieve the filename from command-line arguments.
    file_name = sys.argv[1]

    print(f"{C.BLUE}=== Cyber Archives Recovery ==={C.RESET}")
    print(f"Accessing file '{C.YELLOW}{file_name}{C.RESET}'")

    # Attempt to open and read the file.
    try:
        # Open the file in read mode.
        file_to_read = open(file_name, "r")
        print("---\n")
        # Output the file contents to the terminal.
        print(file_to_read.read())
        print("\n---")
    # Handle possible file access errors and display them.
    except (FileNotFoundError, PermissionError, OSError) as error:
        print(f"Error opening file '{C.RED}{file_name}{C.RESET}': "
              f"{C.BG_RED}{error}{C.RESET}")
    # Ensure the file is properly closed if it was opened.
    finally:
        if file_to_read:
            file_to_read.close()
            print(f"File '{C.YELLOW}{file_name}{C.RESET}' closed.")


if __name__ == "__main__":
    ancient_text()
