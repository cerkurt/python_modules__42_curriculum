#!/usr/bin/env python3

"""
Custom garden error types demo.


This script demonstrates:
- creating custom exception classes
- building an exception hierarchy using inheritance
- raising custom exceptions from functions
- catching specific exceptions and a shared base exception
- continuing program execution after errors occur
"""


class C:
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


class GardenError(Exception):
    """Base class for all custom garden-related errors.

    Inheriting from Exception allows GardenError (and its child classes) to be
    raised and caught using Python's try / except mechanism."""

    def __init__(self, error_message: str = "Caught a garden error:") -> None:
        """Initialize the base garden error with a message."""
        super().__init__(error_message)


class PlantError(GardenError):
    """Error related to plant health or status.

    Used when a plant enters an invalid or dangerous state
    (for example: wilting or fading)."""

    def __init__(self, name: str, status: str) -> None:
        error_message = f"The {name} plant is {status}!"
        super().__init__(error_message)
        self.name = name
        self.status = status


class WaterError(GardenError):
    """Error related to water supply conditions.

    Raised when the water level is unsafe for garden operation."""

    def __init__(self, water_level: str) -> None:
        """Create a WaterError with the current water level."""
        error_message = "Not enough water in the tank!"
        super().__init__(error_message)
        self.water_level = water_level


def plant_status(name: str, status: str) -> None:
    """Check plant status and raise PlantError if unsafe.

    Raises a PlantError when the plant is wilting or fading."""
    if status == "wilting" or status == "fading":
        raise PlantError(name, status)


def water_level(water_level: str) -> None:
    """Check water level and raise WaterError if unsafe.

    Raises a WaterError when the water level is low or risky."""
    if water_level == "low" or water_level == "risky":
        raise WaterError(water_level)


def garden_error_checks() -> None:
    """Run demonstrations of all custom garden error types.

    Shows how individual custom exceptions can be caught
    as well as how a shared base exception can catch them all."""
    print(f"{C.BLUE}=== Custom Garden Errors Demo ==={C.RESET}\n")

    # Test PlantError specifically
    try:
        print(f"{C.YELLOW}Testing PlantError...{C.RESET}")
        plant_status("Tomato", "wilting")
    except PlantError as e:
        print(f"Caught {C.BG_RED}{type(e).__name__}{C.RESET}: {e}\n")

    # Test WaterError specifically
    try:
        print(f"{C.YELLOW}Testing WaterError...{C.RESET}")
        water_level("low")
    except WaterError as e:
        print(f"Caught {C.BG_RED}{type(e).__name__}{C.RESET}: {e}\n")

    # Test catching all garden-related errors together
    print(f"{C.YELLOW}Testing catching all garden errors...{C.RESET}")

    multiple_test_list = [("tomato", "wilting"), ("water", "low")]
    for case in multiple_test_list:
        try:
            if case[0] == "tomato":
                plant_status(case[0], case[1])
            elif case[0] == "water":
                water_level(case[1])
        except GardenError as e:
            print(f"Caught {C.BG_RED}{type(e).__name__}{C.RESET}: {e}")

    print(f"\n{C.BLUE}All custom error types work correctly!{C.RESET}")


if __name__ == "__main__":
    garden_error_checks()
