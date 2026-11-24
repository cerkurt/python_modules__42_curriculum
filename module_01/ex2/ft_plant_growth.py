#!/usr/bin/env python3
"""
Weekly plant growth simulation.

This script demonstrates:
- defining a class with multiple attributes
- updating object state over time (age and height)
- calling methods repeatedly inside loops
- separating simulation logic into helper functions
"""


class Plant:
    """Represent a plant that grows by a fixed amount each day.

    The Plant class stores basic data (name, height, age, daily growth) and
    provides methods to update and display this data over time.
    """
    def __init__(self, name: str, height: int, age: int,
                 daily_growth: int) -> None:
        """Initialize a Plant instance.

        The constructor stores the initial state of the plant.
        params:
            name (str): Name of the plant.
            height (int): Height of the plant in centimeters.
            age (int): Age of the plant in days.
            daily_growth (int): Amount of growth in a day.
        """
        self.name = name
        self.height = height
        self.age = age
        self.daily_growth = daily_growth

    def age_daily(self) -> None:
        """Simulate one day passing by increasing the plant's age."""
        self.age += 1
        return None

    def grow(self) -> None:
        """Simulate one day of growth by increasing the plant's height."""
        self.height += self.daily_growth
        return None

    def get_info(self) -> None:
        """Display the plant's current state.

        This method reads the attributes stored in the object and prints them.
        """
        print(f"{self.name}: {self.height} cm, {self.age} days old, "
              f"with {self.daily_growth} cm grow today.")
        return None


def weekly_grow(garden: list) -> None:
    """Simulate one week of growth for all plants in the garden.

    Each day:
    - current plant information is printed
    - height and age are updated

    At the end, a weekly growth summary is displayed.
    """
    # Store starting heights so we can calculate total weekly growth
    begin_height = {plant.name: plant.height for plant in garden}
    # Simulate growth for 7 consecutive days
    n = 1
    while n <= 7:
        print(f"\n=== Day {n} ===\n")
        # Show today's status before updating the plant
        for plant in garden:
            plant.get_info()
            plant.grow()
            plant.age_daily()
        n += 1

    print("\n=== Weekly Report ===\n")
    # Compare final height with starting height to get weekly growth
    for plant in garden:
        # Total growth over the week for the current plant.
        weekly_grow = plant.height - begin_height[plant.name]
        print(f"Growth report of this week for {plant.name}: "
              f"+{weekly_grow} cm total")
    return None


def main():
    """Create sample Plant objects and run the weekly simulation."""
    # Create example plants with different growth rates
    rose = Plant("Rose", 25, 30, 3)
    sunflower = Plant("Sunflower", 40, 6, 5)
    cactus = Plant("Cactus", 5, 18, 1)

    garden = [rose, sunflower, cactus]
    weekly_grow(garden)


if __name__ == "__main__":
    main()
