#!/usr/bin/env python3

"""Read, transform, and optionally save archive data using standard streams."""

import sys


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def stream_management() -> None:
    """Process archive data while using stdin, stdout, and stderr
    explicitly."""

    # Initialize file handler to safely manage it in finally block.
    file_to_read = None

    # Ensure exactly one filename argument is provided.
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <file>\n")
        return

    # Retrieve the filename from command-line arguments.
    file_name = sys.argv[1]

    # Send the system header and target file information through stdout.
    sys.stdout.write(
        f"{C.BLUE}=== Cyber Archives Recovery & Preservation ==={C.RESET}\n"
    )
    sys.stdout.write(f"Accessing file '{C.YELLOW}{file_name}{C.RESET}'\n")

    # Attempt to open and read the source file.
    try:
        # Open the file in read mode.
        file_to_read = open(file_name, "r")

        # Read the entire file content into memory.
        content = file_to_read.read()

        # Output the original file content through stdout.
        sys.stdout.write("---\n\n")
        sys.stdout.write(content)
        sys.stdout.write("\n---\n")

    # Send file access errors through stderr.
    except (FileNotFoundError, PermissionError, OSError) as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{C.RED}{file_name}{C.RESET}': "
            f"{C.BG_RED}{error}{C.RESET}\n")
        return

    # Ensure the file is properly closed if it was opened.
    finally:
        if file_to_read:
            file_to_read.close()
            sys.stdout.write(
                f"File '{C.YELLOW}{file_name}{C.RESET}' closed.\n\n")

    # Split content into lines for transformation.
    transformed_lines = content.splitlines()

    # Prepare a string to store transformed lines.
    transformed_content = ""

    # Append '#' to each line to create transformed content.
    for line in transformed_lines:
        transformed_content += line + "#\n"

    # Display the transformed content through stdout.
    sys.stdout.write("Transform data:\n")
    sys.stdout.write("---\n\n")
    sys.stdout.write(transformed_content)
    sys.stdout.write("\n---\n")

    # Prompt user through stdout before reading from stdin.
    sys.stdout.write("Enter new file name (or empty): ")

    # Flush stdout so the prompt appears before waiting for input.
    sys.stdout.flush()

    # Read the optional output filename directly from stdin.
    new_file_name = sys.stdin.readline().strip()

    # If no filename is provided, skip saving.
    if new_file_name == "":
        sys.stdout.write("Data not saved.\n")
        return

    # Initialize write handler to safely manage it in finally block.
    write_file = None

    # Attempt to save transformed content to a new file.
    try:
        # Inform the user that saving is about to begin.
        sys.stdout.write(
            f"Saving data to '{C.YELLOW}{new_file_name}{C.RESET}'\n")

        # Open the new file in write mode.
        write_file = open(new_file_name, "w")

        # Write transformed content into the file.
        write_file.write(transformed_content)
        sys.stdout.write(
            f"Data saved in file '{C.YELLOW}{new_file_name}{C.RESET}'.\n")

    # Send file saving errors through stderr.
    except (PermissionError, OSError) as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{C.RED}{new_file_name}{C.RESET}': "
            f"{C.BG_RED}{error}{C.RESET}\n")
        sys.stdout.write("Data not saved.\n")

    # Ensure the output file is properly closed if it was opened.
    finally:
        if write_file:
            write_file.close()


if __name__ == "__main__":
    stream_management()
