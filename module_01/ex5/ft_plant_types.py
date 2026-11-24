#!/usr/bin/env python3
"""
Garden plant types demo.

This script demonstrates:
- inheritance (Flower, Tree, Vegetable share a common Plant base class)
- method overriding (each child class has its own create() behavior)
- using helper methods (bloom(), shade(), nutrition())
- validating input before creating objects using an error_list
"""
import math


class C:
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    BG_RED = "\033[41m"


class Plant:
    """Base class for all plant types.

    Stores shared attributes (name, height, age) and provides a default
    create() method that can be reused or overridden by subclasses.
    Note:
        Input validation happens in main() using an error_list.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant.

        Stores basic plant data that is shared by all child classes."""
        # Store shared attributes for all plant types
        self.name = name
        self.height = height
        self.age = age

    @property
    def height(self) -> int:
        """Return height in centimeters."""
        return self._height

    @height.setter
    def height(self, input_height: int) -> None:
        """Store height (validation happens in main)."""
        self._height = input_height
        return None

    @property
    def age(self) -> int:
        """Return age in days."""
        return self._age

    @age.setter
    def age(self, input_age: int) -> None:
        """Store age (validation happens in main)."""
        self._age = input_age
        return None

    def create(self) -> None:
        """Print basic plant information."""
        print(f"{C.YELLOW}{self.name}{C.RESET}: "
              f"{self.height}cm, {self.age} days")


# Inheritance example:
# Flower inherits from Plant, so it automatically gets Plant's attributes
# and methods (name, height, age). Flower then adds its own attribute (color).
class Flower(Plant):
    """Flower plant type.
    Adds a color attribute and overrides create() to show bloom behavior.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a Flower.

        Extends Plant by adding a color attribute.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Print a bloom message."""
        print(f"{self.name} is {C.GREEN}blooming{C.RESET} beautifully!\n")

    # Method overriding:
    # Flower replaces Plant.create() with its own version.
    def create(self) -> None:
        """Print flower details and trigger blooming."""
        print(f"{C.YELLOW}{self.name} ({self.__class__.__name__}){C.RESET}: "
              f"{self.height}cm ,{self.age} days, {self.color} color.")
        self.bloom()


# Another inheritance example:
# Tree is also a child of Plant. It reuses the shared Plant behavior and
# adds trunk_diameter plus extra methods for shade calculations.
class Tree(Plant):
    """Tree plant type.
    Adds trunk diameter and calculates shade area using simple geometry.
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a Tree.

        Extends Plant by adding trunk diameter.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    @property
    def trunk_diameter(self) -> int:
        """Return trunk diameter in centimeters."""
        return self._trunk_diameter

    @trunk_diameter.setter
    def trunk_diameter(self, input_diameter: int) -> None:
        """Store trunk diameter (validation happens in main)."""
        self._trunk_diameter = input_diameter
        return None

    def shade_area(self) -> float:
        """Calculate and return shade area in square meters."""
        # Convert centimeters to meters for the area calculation
        height_meter = self.height / 100
        trunk_meter = self.trunk_diameter / 100
        crown_diameter = ((15 * trunk_meter) + (2 * height_meter)) / 2
        shade_area = math.pi * (crown_diameter / 2) ** 2
        return shade_area

    def shade(self) -> None:
        """Print the calculated shade area."""
        print(f"{self.name} provides "
              f"{C.GREEN}{self.shade_area():.2f}{C.RESET} "
              f"square meters of shade.\n")

    # Method overriding:
    # Tree provides its own create() and calls shade() for extra output.
    def create(self) -> None:
        """Print tree details and shade information."""
        print(f"{C.YELLOW}{self.name} ({self.__class__.__name__}){C.RESET}: "
              f"{self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter.")
        self.shade()


# Third inheritance example:
# Vegetable inherits from Plant and adds harvest_season and nutrition().
class Vegetable(Plant):
    """Vegetable plant type.
    Adds a harvest season and overrides create() to show nutrition info.
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str) -> None:
        """Initialize a Vegetable.
        Extends Plant by adding a harvest season.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutrition(self) -> None:
        """Print nutritional information."""
        print(f"{self.name} is rich in {C.GREEN}vitamin C{C.RESET}.\n")

    # Method overriding:
    # Vegetable customizes create() and calls nutrition() for extra output.
    def create(self) -> None:
        """Print vegetable details and nutrition information."""
        print(f"{C.YELLOW}{self.name} ({self.__class__.__name__}){C.RESET}: "
              f"{self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest.")
        self.nutrition()


def main():
    """Create sample plants and display their behavior.
    Inputs are validated before object creation. Invalid entries are rejected
    using an error_list (no exceptions needed).
    """

    print(f"{C.BLUE}=== Garden Plant Types ==={C.RESET}")

    # Flowers: (name, height_cm, age_days, color)
    flower_check_list = [
        ("Rose", 35, 12, "red"),
        ("Tulip", 28, 20, "yellow"),
        ("Lily", 40, 18, "white"),
    ]

    # Trees: (name, height_cm, age_days, trunk_diameter_cm)
    tree_check_list = [
        ("Oak", 500, 1825, 50),
        ("Pine", 420, 1500, 35),
    ]

    # Vegetables: (name, height_cm, age_days, harvest_season)
    vegetable_check_list = [
        ("Orange", 80, 90, "autumn"),
        ("Carrot", 30, 70, "winter"),
        ("Bell pepper", 60, 85, "summer"),
        # Uncomment to test rejection:
        # ("Bad Carrot", -3, 10, "winter"),
    ]

    # Checklist for flowers (validated before creation)
    flower_list = []
    for (name, height_cm, age_days, color) in flower_check_list:
        error_list = []

        if height_cm < 0:
            error_list.append(
                f"Invalid operation attempted: height {height_cm}cm "
                f"{C.BG_RED}[REJECTED]{C.RESET}\n"
                f"Security: Negative height rejected!")

        if age_days < 0:
            error_list.append(
                f"Invalid operation attempted: age {age_days} days "
                f"{C.BG_RED}[REJECTED]{C.RESET}\n"
                f"Security: Negative age rejected!")

        if error_list:
            print(f"\nCreating {C.YELLOW}{name}{C.RESET}...")
            print(f"{C.BG_RED}Error{C.RESET} during creation of {name} :(")
            for error_message in error_list:
                print(error_message)
            continue
        # Only create the object when the input is considered safe
        flower_list.append(Flower(name, height_cm, age_days, color))

    # Checklist for trees (validated before creation)
    tree_list = []
    for (name, height_cm, age_days, trunk_cm) in tree_check_list:
        error_list = []

        if height_cm < 0:
            error_list.append(
                f"Invalid operation attempted: height {height_cm}cm "
                f"{C.BG_RED}[REJECTED]{C.RESET}\n"
                f"Security: Negative height rejected!")

        if age_days < 0:
            error_list.append(
                f"Invalid operation attempted: age {age_days} days "
                f"{C.BG_RED}[REJECTED]{C.RESET}\n"
                f"Security: Negative age rejected!")

        if trunk_cm < 0:
            error_list.append(
                f"Invalid operation attempted: trunk {trunk_cm}cm "
                f"{C.BG_RED}[REJECTED]{C.RESET}\n"
                f"Security: Negative diameter rejected!")

        if error_list:
            print(f"\nCreating {C.YELLOW}{name}{C.RESET}...")
            print(f"{C.BG_RED}Error{C.RESET} during creation of {name} :(")
            for error_message in error_list:
                print(error_message)
            continue
        # Only create the object when the input is considered safe
        tree_list.append(Tree(name, height_cm, age_days, trunk_cm))

    # Checklist for vegetables (validated before creation)
    vegetable_list = []
    for (name, height_cm, age_days, season) in vegetable_check_list:
        error_list = []

        if height_cm < 0:
            error_list.append(
                f"Invalid operation attempted: height {height_cm}cm "
                f"{C.BG_RED}[REJECTED]{C.RESET}\n"
                f"Security: Negative height rejected!")

        if age_days < 0:
            error_list.append(
                f"Invalid operation attempted: age {age_days} days "
                f"{C.BG_RED}[REJECTED]{C.RESET}\n"
                f"Security: Negative age rejected!")

        # If any errors were found, reject object creation and move on
        if error_list:
            print(f"\nCreating {C.YELLOW}{name}{C.RESET}...")
            print(f"{C.BG_RED}Error{C.RESET} during creation of {name} :(")
            for error_message in error_list:
                print(error_message)
            continue
        # Only create the object when the input is considered safe
        vegetable_list.append(Vegetable(name, height_cm, age_days, season))

    # Display all created plants
    garden = [flower_list, tree_list, vegetable_list]

    # Polymorphism:
    # Even though we call the same method name (create()) on each object,
    # Python runs the correct version depending on the plant's class.
    for plant_list in garden:
        for plant in plant_list:
            plant.create()


if __name__ == "__main__":
    main()
