#!/usr/bin/env python3
"""
Garden error types demo.

This script demonstrates:
- defining functions that deliberately trigger different exceptions
- catching specific exception types using multiple except blocks
- handling multiple exception types together in a single except clause
- keeping a program running after errors occur
"""


class C:
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def garden_operations() -> list:
    """Return a list of error test cases.

    Each entry contains:
    - the name of an exception type
    - a function that triggers that exception when called

    These functions are used to demonstrate how different errors can be caught
    and handled.
    """

    # This function triggers a ValueError by converting invalid input.
    def case_value_error():
        int("hello")

    # This function triggers a ZeroDivisionError by dividing by zero.
    def case_zero_division_error():
        4242 / 0

    # This function triggers a FileNotFoundError by opening a missing file.
    def case_file_not_found_error():
        open("cant_touch_this.txt")

    # This function triggers a KeyError by accessing a missing dictionary key.
    def case_key_error():
        garden = {"rose": 1}
        garden["missing_plant"]

    return [("ValueError", case_value_error),
            ("ZeroDivisionError", case_zero_division_error),
            ("FileNotFoundError", case_file_not_found_error),
            ("KeyError", case_key_error)]


def test_error_types():
    """Test and display handling of different exception types.

    Iterates over all error cases returned by garden_operations() and shows how
    each exception is caught separately.
    """
    print(f"{C.BLUE}=== Garden Error Types Demo ==={C.RESET}")

    # Loop through each error case and test it individually.
    for name, case in garden_operations():
        print(f"\n{C.YELLOW}Testing {name}...{C.RESET}")
        # Run the test case inside a try block.
        try:
            case()
        # Catch and handle ValueError specifically.
        except ValueError as error:
            print(f"Caught {C.BG_RED}{name}{C.RESET}: "
                  f"{error}")

        except ZeroDivisionError as error:
            print(f"Caught {C.BG_RED}{name}{C.RESET}: "
                  f"{error}")

        except FileNotFoundError as error:
            print(f"Caught {C.BG_RED}{name}{C.RESET}: "
                  f"No such file. Missing {error.filename}")

        except KeyError as error:
            print(f"Caught {C.BG_RED}{name}{C.RESET}: "
                  f"{error}")

    print("\nTesting multiple errors togerher...")
    # Catch multiple different exceptions using a single except clause.
    try:
        garden_operations()[0][1]()
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues! :)")

    print(f"\n{C.BLUE}All error types tested successfully!{C.RESET}")


if __name__ == "__main__":
    test_error_types()
