#!/usr/bin/env python3
"""
Garden temperature checker.

This script demonstrates:
- converting user input from string to integer
- handling invalid input using try / except
- using ValueError to catch conversion errors
- keeping a program running even when bad input is given
"""


class C:
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def check_temperature(temp_str: str) -> None:
    """Check a single temperature value.

    Tries to convert the input string to an integer and prints a message
    describing whether the temperature is suitable for plants.

    Invalid input is handled using try / except so the program does not crash.
    """
    try:
        # Attempt to convert the input string into an integer.
        test_input = int(temp_str)
        print(f"\nTesting temperature: {C.YELLOW}{test_input}°C{C.RESET}...")
        # Valid temperature ranges are checked using conditional statements.
        if test_input >= 0 and test_input <= 40:
            print(f"Temperature {C.GREEN}{test_input}{C.RESET} is "
                  f"{C.GREEN}perfect{C.RESET} for plants!\n")

        elif test_input > 40:
            print(f"{C.BG_RED}Error:{C.RESET} {C.RED}{test_input}{C.RESET} is "
                  f"too {C.RED}hot{C.RESET} for plants! (max 40°C)\n")

        else:
            print(f"{C.BG_RED}Error:{C.RESET} {C.BLUE}{test_input}{C.RESET} "
                  f"is too {C.BLUE}cold{C.RESET} for plants! (min 0°C)\n")

    # This block runs only if int(temp_str) fails
    except ValueError:
        print(f"\nTesting temperature: {C.YELLOW}{temp_str}°C{C.RESET}...")
        print(f"{C.BG_RED}Error:{C.RESET} {C.BG_RED}{temp_str}{C.RESET} "
              f"is not a valid number! :(")
    return None


def test_temperature_input() -> None:
    """Repeatedly ask the user for temperature input. Continues running until
    the user types 'q'.

    Demonstrates how exceptions allow the loop to keep running even when
    invalid input is entered.
    """
    print(f"{C.YELLOW}=== Garden Temperature Checker ==={C.RESET}")
    print(f"Type {C.YELLOW}'q'{C.RESET} to quit anytime :)")

    # Keep asking for input until the user chooses to quit
    while True:
        value = input("Please enter a temperature value:")
        # Special case: user wants to exit the program
        if value == 'q':
            print("Goodbye!")
            break
        # Validate and handle the entered temperature safely
        check_temperature(value)
    print("All tests completed- program didn't crash!")
    return None


if __name__ == "__main__":
    test_temperature_input()
