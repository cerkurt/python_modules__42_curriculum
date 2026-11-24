#!/usr/bin/env python3
"""
Simple garden data demo.

This script demonstrates:
- defining a basic class
- using __init__ as a constructor
- storing data in object attributes
- calling methods on objects
"""


class Plant:
    """Represent a plant with basic data.

    This class stores simple attributes (name, height, age) and provides a
    method to display them.
    """
    # __init__ is the constructor: it runs automatically when an object is
    # created
    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant instance.
        params:
            name (str): Name of the plant.
            height (int): Height of the plant in centimeters.
            age (int): Age of the plant in days.
        """
        # Store incoming values as object attributes
        self.name = name
        self.height = height
        self.age = age

    # methods: functions that perform specific actions on the objects.
    def garden(self):
        """Display the plant's stored data.

        This method reads the attributes set during initialization and prints
        them in a formatted way.
        """
        # Use the attributes defined in __init__
        print(f"{self.name}: {self.height} cm, {self.age} days old")


def main():
    """Create Plant objects and demonstrate method calls.

    This function acts as the entry point for the script:
    - objects are created from the Plant class
    - their methods are called to display data
    """
    # Create Plant objects using the class
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant1.garden()
    plant2.garden()
    plant3.garden()


if __name__ == "__main__":
    main()
