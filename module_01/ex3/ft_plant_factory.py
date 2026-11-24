#!/usr/bin/env python3
"""
Simple plant factory demo.

This script demonstrates:
- creating multiple objects from the same class
- storing objects in a list (garden)
- passing a list of objects to a function
- iterating over objects and calling their methods
"""


class Plant:
    """Represent a plant created by the factory.

    Stores basic attributes (name, height, age) and provides a method to
    confirm creation.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance.

        The constructor stores the plant's initial data when the object is
        created.
        params:
            name (str): Name of the plant.
            height (int): Height of the plant in centimeters.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def create(self) -> None:
        """Display a confirmation message for this plant.

        Called when iterating over the garden list.
        """
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def output(garden: list) -> None:
    """Display all plants created by the factory. Iterates over the garden list
    and calls create() on each Plant object."""

    # Loop through each Plant object in the garden list
    for plant in garden:
        plant.create()


def main():
    """Create Plant objects and display a factory summary."""

    # Create multiple Plant objects using the same class
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 100, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    # Group all created plants into a single garden list
    garden = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    output(garden)

    # Count how many plants were created using the list length
    n = len(garden)
    print(f"\nTotal plants created: {n}")


if __name__ == "__main__":
    main()
