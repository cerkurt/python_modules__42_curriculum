#!/usr/bin/env python3

"""
Garden plant health checker demo.

This script demonstrates:
- raising ValueError when input is invalid (fail fast)
- writing clear validation rules (min/max checks)
- catching errors in a test function so the program continues
- separating validation logic from demo/testing
"""


class C:
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> None:
    """Validate plant health inputs and raise errors for invalid values.

    This function demonstrates "raising" exceptions:
    - If an input is invalid, we stop immediately by raising ValueError.
    - If everything is valid, we print success messages.
    """

    # Convert the incoming name to a string to avoid unexpected types.
    name = str(plant_name)
    # Rule 1: name cannot be empty
    if name == "":
        raise ValueError("Plant name cannot be empty!")

    max_water = 10
    min_water = 1
    # Rule 2: water level must stay within a safe range
    if water_level < min_water or water_level > max_water:
        # Raise a specific error message depending on which side failed
        if water_level < min_water:
            raise ValueError(f"Water level {water_level} is too low! "
                             f"(min {min_water})")
        elif water_level > max_water:
            raise ValueError(f"Water level {water_level} is too high! "
                             f"(max {max_water})")

    max_sun = 12
    min_sun = 2
    # Rule 3: sunlight hours must stay within a safe range
    if sunlight_hours < min_sun or sunlight_hours > max_sun:
        # Raise a specific error message depending on which side failed
        if sunlight_hours < min_sun:
            raise ValueError(f"Sunlight hours {sunlight_hours} is "
                             f"too low (min {min_sun})")
        elif sunlight_hours > max_sun:
            raise ValueError(f"Sunlight hours {sunlight_hours} is "
                             f"too high (max {max_sun})")

    # If we reach this point, all checks passed
    print(f"Plant {name} is healthy!")
    print(f"Water level {water_level} is optimal!")
    print(f"{sunlight_hours} hour of sun is awesome!")


def test_plant_checks() -> None:
    """Run a set of test cases to demonstrate raising and catching errors.

    Each test calls check_plant_health() inside a try block. If ValueError is
    raised, the except block prints the error message and the program continues
    to the next test."""

    print(f"{C.BLUE}=== Garden Plant Health Checker ==={C.RESET}")

    print(f"\n{C.YELLOW}Testing with good values...{C.RESET}")
    try:
        check_plant_health("tomato", 6, 8)
    except ValueError as error:
        print(f"{C.BG_RED}Error: {C.RESET} {error}")

    print(f"\n{C.YELLOW}Testing empty plant name...{C.RESET}")
    try:
        check_plant_health("", 2, 7)
    except ValueError as error:
        print(f"{C.BG_RED}Error:{C.RESET} {error}")

    print(f"\n{C.YELLOW}Testing bad water level...{C.RESET}")
    try:
        check_plant_health("tomato", 12, 5)
    except ValueError as error:
        print(f"{C.BG_RED}Error:{C.RESET} {error}")

    print(f"\n{C.YELLOW}Testing bad sunlight hours...{C.RESET}")
    try:
        check_plant_health("tomato", 4, 34)
    except ValueError as error:
        print(f"{C.BG_RED}Error:{C.RESET} {error}\n")


if __name__ == "__main__":
    test_plant_checks()
