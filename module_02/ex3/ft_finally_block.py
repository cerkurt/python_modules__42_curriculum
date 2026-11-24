#!/usr/bin/env python3

"""
Garden watering system demo using try / except / finally.


This script demonstrates:
- raising an exception from a method
- catching exceptions during iteration
- using a finally block for guaranteed cleanup
- the fact that finally always executes, even when errors occur
"""


class C:
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def water_plants(plant_list: list) -> None:
    """Water all plants in the provided list.

    Demonstrates how:
        - try protects the main operation,
        - except handles errors,
        - finally performs cleanup regardless of success or failure."""
    print("Opening Watering System")

    error_check = False
    try:
        # Attempt to water each plant in the list
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError("invalid plant")

            print(f"Watering {C.YELLOW}{plant}{C.RESET}")
        # Runtime validation to deliberately trigger an exception
    except ValueError as error:
        error_check = True
        # Handle invalid plant error
        print(f"Cannot water {C.BG_RED}{plant}{C.RESET} - {error}")
    finally:
        # This block ALWAYS runs, even if an error occurred above
        print(f"Closing watering system {C.YELLOW}(cleanup){C.RESET}\n")

    if error_check is True:
        print(f"{C.BLUE}Cleanup always happens, even with errors!{C.RESET}")

    if error_check is False:
        print(f"{C.GREEN}Watering completed successfully!{C.RESET}\n")


def test_watering_system() -> None:
    """Run two watering scenarios: one valid, one with an error."""

    print(f"{C.BLUE}=== Garden Watering System ===\n{C.RESET}")

    # Scenario 1: all plants are valid
    plant_list_1 = ["tomato", "carrot", "lettuce", "plum"]
    print("Testing normal watering...")
    water_plants(plant_list_1)

    # Scenario 2: one plant is invalid (name is None)
    plant_list_2 = ["tomato", "carrot", None, "plum"]
    print("Testing with error...")
    water_plants(plant_list_2)


if __name__ == "__main__":
    test_watering_system()
