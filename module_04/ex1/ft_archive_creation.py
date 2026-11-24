#!/usr/bin/env python3

"""Read an archive file, transform its lines, and optionally save the
result."""

import sys


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def archive_creation() -> None:
    """Read archive data, append # to each line, and optionally save it."""

    # Initialize file handler to safely manage it in finally block.
    file_to_read = None

    # Ensure exactly one filename argument is provided.
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    # Retrieve the filename from command-line arguments.
    file_name = sys.argv[1]

    # Display system header and target file information.
    print(f"{C.BLUE}=== Cyber Archives Recovery & Preservation ==={C.RESET}")
    print(f"Accessing file '{C.YELLOW}{file_name}{C.RESET}'")
    print("---\n")

    # Attempt to open and read the source file.
    try:
        # Open the file in read mode.
        file_to_read = open(file_name, "r")
        # Read the entire file content into memory.
        content = file_to_read.read()
        # Output the original file content.
        print(content)
        print("\n---")

    # Handle file access errors and display them.
    except (FileNotFoundError, PermissionError, OSError) as error:
        print(f"Error opening file '{C.RED}{file_name}{C.RESET}': "
              f"{C.BG_RED}{error}{C.RESET}")
        return

    # Ensure the file is properly closed if it was opened.
    finally:
        if file_to_read:
            file_to_read.close()
            print(f"File '{C.YELLOW}{file_name}{C.RESET}' closed.\n")

    # Split content into lines for transformation.
    transformed_lines = content.splitlines()

    # Prepare a string to store transformed lines.
    transformed_content = ""
    # Append '#' to each line to create transformed content.
    for line in transformed_lines:
        transformed_content += line + "#\n"

    # Display the transformed content.
    print("Transform data:")
    print("---\n")
    print(transformed_content, end="")
    print("\n---")

    # Prompt user for optional output filename.
    new_file_name = input("Enter new file name (or empty): ")

    # If no filename is provided, skip saving.
    if new_file_name == "":
        print("Not saving data.")
        return

    # Attempt to save transformed content to a new file.
    try:
        print(f"Saving data to '{new_file_name}'")

        # Open the new file in write mode.
        write_file = open(new_file_name, "w")

        # Write transformed content into the file.
        write_file.write(transformed_content)

        # Close the file after writing.
        write_file.close()
        print(f"Data saved in file '{new_file_name}'.")

    # Handle errors during file saving.
    except (PermissionError, OSError) as error:
        print(f"Error saving file '{new_file_name}': {error}")


if __name__ == "__main__":
    archive_creation()
