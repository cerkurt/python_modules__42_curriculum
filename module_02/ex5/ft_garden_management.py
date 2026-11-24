#!/usr/bin/env python3
"""
Garden management system demo.

This script demonstrates:
- defining and raising custom exceptions
- building a small exception hierarchy (GardenError -> PlantError)
- using try / except / finally inside class methods
- handling errors both locally and at a higher level
- keeping the program running after errors occur
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
    """Base exception for all garden-related errors.

    Inheriting from Exception allows garden-specific error to be grouped and
    caught together."""
    def __init__(self, error_message: str) -> None:
        super().__init__(error_message)


class PlantError(GardenError):
    """Exception related to invalid plant operations.

    Used when plant name, water level, or sunlight values are invalid."""
    def __init__(self, error_message: str) -> None:
        super().__init__(error_message)


class GardenManager():
    """Provide basic garden management operations.

    This class groups together actions such as:
    - adding plants
    - watering plants
    - checking plant health

    Each method demonstrates a different way of handling errors.
    """
    def add_plant(self, plant_name: str) -> None:
        """Add a plant to the garden.

        Raises PlantError if the plant name is invalid.
        """
        # Validate plant name before performing the operation
        if not isinstance(plant_name, str):
            raise PlantError("Invalid plant name!")
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        print(f"Added {C.YELLOW}{plant_name}{C.RESET} successfully.")

    def water_plant(self, plant_name: str) -> None:
        """Water a single plant safely.

        Demonstrates local try / except / finally handling
        inside a class method.
        """
        # Track whether an error occurred during watering
        print("Opening Watering System")
        error_check = False
        # Protect the watering operation using try / except / finally
        try:
            if not isinstance(plant_name, str):
                raise PlantError("Invalid plant name!")
            if plant_name == "":
                raise PlantError("Plant name cannot be empty!")

            print(f"Watering {C.YELLOW}{plant_name}{C.RESET}")

        except GardenError as error:
            error_check = True

            print(f"{C.BG_RED}Error with {plant_name}:{C.RESET} Cannot water -"
                  f" {error}")
        # Cleanup code that always runs, even when an error occurs
        finally:
            print(f"Closing watering system {C.YELLOW}(cleanup){C.RESET}")

        if error_check is True:
            print(f"{C.BLUE}Cleanup always happens, "
                  f"even with errors!{C.RESET}\n")

        if error_check is False:
            print(f"{C.GREEN}Watering completed successfully!{C.RESET}\n")

    def plant_health(self, plant_name: str, water_level: int,
                     sunlight: int) -> None:
        """Check plant health values.

        Raises PlantError when water or sunlight values are outside safe
        limits."""
        if not isinstance(plant_name, str):
            raise PlantError("Invalid plant name!")
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")

        # Validate water level against safe limits
        max_water = 10
        min_water = 1

        if water_level < min_water or water_level > max_water:
            if water_level < min_water:
                raise PlantError(f"water level {water_level} is too low "
                                 f"(min {min_water})\n")
            elif water_level > max_water:
                raise PlantError(f"water level {water_level} is too high "
                                 f"(min {min_water})\n")

        # Validate sunlight hours against safe limits
        max_sun = 12
        min_sun = 2

        if sunlight < min_sun or sunlight > max_sun:

            if sunlight < min_sun:
                raise PlantError(f"sunlight hours {sunlight} is too low "
                                 f"(min {min_sun})\n")
            elif sunlight > max_sun:
                raise PlantError(f"sunlight hours {sunlight} is too high "
                                 f"(max {max_sun})\n")

        print(f"{C.YELLOW}{plant_name}:{C.RESET} healthy! "
              f"(water: {water_level}, sun: {sunlight})")


def garden_management():
    """Run a full garden management demo.

    Demonstrates adding plants, watering them, and checking plant health while
    handling errors."""
    print(f"{C.BLUE}=== Garden Management System ==={C.RESET}\n")

    # Create a GardenManager instance to manage operations
    plant = GardenManager()
    # List of plant names (includes invalid entries for testing)
    plant_list_1 = [None, "carrot", "lettuce", "plum"]
    print("Adding plants to garden...")
    # Attempt to add plants and catch errors at a higher level
    for plant_name in plant_list_1:
        try:
            plant.add_plant(plant_name)
        except PlantError as error:
            print(f"{C.BG_RED}Error adding plant:{C.RESET} {error}")

    print("\nWatering plants...")
    # Water plants using internal error handling in water_plant()
    for plant_name in plant_list_1:
        try:
            plant.water_plant(plant_name)
        except GardenError as error:
            print(f"{C.BG_RED}Error with {plant_name}:{C.RESET} {error}")

    # Plant health test data: (name, water level, sunlight)
    plant_list_2 = [("tomato", -8, 5), ("carrot", 5, -12), ("lettuce", 2, 6),
                    ("plum", 45, 4)]
    print("Checking plant health...")
    for plant_name, water_level, sunlight in plant_list_2:
        try:
            print(f"Checking {C.YELLOW}{plant_name}{C.RESET}")
            plant.plant_health(plant_name, water_level, sunlight)
        except PlantError as error:
            print(f"{C.BG_RED}Error checking {plant_name}:{C.RESET} {error}")


if __name__ == "__main__":
    garden_management()
