#!/usr/bin/env python3

"""Safely read from or write to archive files using a context manager."""


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def secure_archive(filename: str,
                   action: int | str = "read",
                   content: str = "") -> tuple[bool, str]:
    """Safely read from or write to an archive file using with."""

    # Handle read operations (default behavior).
    if action == 0 or action == "read":
        # Open the file safely in read mode using a context manager.
        try:
            with open(filename, "r") as archive_file:
                return (True, archive_file.read())

        # Return failure status and error message if reading fails.
        except (FileNotFoundError, PermissionError, OSError) as error:
            return (False, str(error))

    # Handle write operations.
    if action == 1 or action == "write":
        # Open the file safely in write mode using a context manager.
        try:
            with open(filename, "w") as archive_file:
                # Write the provided content into the file.
                archive_file.write(content)
            return (True, "Content successfully written to file")

        # Return failure status and error message if writing fails.
        except (FileNotFoundError, PermissionError, OSError) as error:
            return (False, str(error))

    # Handle unsupported action values.
    return (False, f"{C.RED}Unknown action{C.RESET}")


def main() -> None:
    """Demonstrate secure archive access for read and write operations."""

    print(f"{C.BLUE}=== Cyber Archives Security ==={C.RESET}\n")

    # Demonstrate reading from a nonexistent file.
    print(f"Using '{C.YELLOW}secure_archive{C.RESET}' to read from "
          f"a nonexistent file:")
    print(f"{secure_archive('/not/existing/file')}\n")

    # Demonstrate reading from an inaccessible file.
    print(f"Using '{C.YELLOW}secure_archive{C.RESET}' to read from "
          f"an inaccessible file:")
    print(f"{secure_archive('/etc/master.passwd')}\n")

    # Demonstrate reading from a valid file.
    print(f"Using '{C.YELLOW}secure_archive{C.RESET}' to read from "
          f"a regular file:")
    print(f"{secure_archive('ancient_fragment.txt')}\n")

    # Demonstrate writing previously read content into a new file.
    print(f"Using '{C.YELLOW}secure_archive{C.RESET}' to write previous "
          f"content to a new file:")

    # Attempt to read data that will be reused for writing.
    success, data = secure_archive("ancient_fragment.txt")

    # If read was successful, proceed with write operation.
    if success:
        print(secure_archive("secure_copy.txt", "write", data))

    # If read failed, display the error information.
    else:
        print((False, data))


if __name__ == "__main__":
    main()
