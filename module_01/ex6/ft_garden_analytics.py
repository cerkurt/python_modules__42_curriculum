#!/usr/bin/env python3
""""
Garden analytics demo.

This script demonstrates:
- Inheritance (Plant -> FloweringPlant -> PrizeFlower, plus Tree)
- Grouping plants into separate gardens by manager name
- A GardenManager class that holds multiple gardens
- A nested GardenStats helper class for computing statistics
- Different method types:
  - instance methods (work on a GardenManager object)
  - class methods (build a manager from raw data)
  - static methods (utility/statistics that don't need self)
- "Security" validation: inputs are checked before objects are created
  using an error_list.
"""


class C:
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    BG_RED = "\033[41m"


class Plant:
    """ Base plant model.
    Stores shared attributes (name, height, manager) and provides common
    behavior like growth calculation and formatted output.
    Note:
        This exercise validates input *before* object creation (in
        create_garden_list)..
    """

    def __init__(self, name: str, height: int, manager: str) -> None:
        """Initialize a plant with name, height (cm), and manager."""
        # Basic attributes shared by all plant types
        self.name = name
        self.height = height
        self.manager = manager

    @property
    def height(self) -> int:
        """Return the height of the plant in centimeters."""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        # Setters just store values; create_garden_list() performs validation.
        self._height = value

    def growth(self) -> float:
        """Calculate and return the growth amount (height/10)."""
        return self.height / 10

    def create(self) -> str:
        """Return a formatted string describing the plant."""
        return f"- {C.YELLOW}{self.name}{C.RESET}: {self.height}cm"

    def growth_display(self) -> None:
        """Print how much the plant grew."""
        print(f"{self.name} grew {self.growth():.0f}cm.")

    def plant_add(self) -> None:
        """Print confirmation that the plant was added to a garden."""
        print(f"Added {C.YELLOW}{self.name}{C.RESET} to "
              f"{C.GREEN}{self.manager}{C.RESET}'s garden.")


# Inheritance example:
# Tree *inherits* from Plant, meaning it automatically gets all Plant
# attributes and methods (name, height, manager, growth(), etc.).
class Tree(Plant):
    """Tree plant type.
    Inherits from Plant without adding new fields."""
    pass


# FloweringPlant is another child class of Plant.
# It reuses Plant behavior and adds new data (color) and behavior.
class FloweringPlant(Plant):
    """Flowering plant with color. Adds a color attribute and extends the base
    create() output."""

    def __init__(self, name: str, height: int, manager: str,
                 color: str) -> None:
        """Initialize with name, height, manager, and flower color."""
        super().__init__(name, height, manager)
        self.color = color

    def create(self) -> str:
        """Return a formatted string with color info added."""
        return super().create() + f", {self.color} flowers blooming"


# PrizeFlower demonstrates multi-level inheritance:
# PrizeFlower -> FloweringPlant -> Plant
class PrizeFlower(FloweringPlant):
    """Flowering plant that gives prize points. Extends FloweringPlant with
    prize points."""

    def __init__(self, name: str, height: int, manager: str, color: str,
                 prize_point: int) -> None:
        """Initialize with name, height, manager, color, and prize points."""
        super().__init__(name, height, manager, color)
        self.prize_point = prize_point

    @property
    def prize_point(self) -> int:
        """Return the prize points awarded to the flower."""
        return self._prize_point

    @prize_point.setter
    def prize_point(self, value: int) -> None:
        # Setters just store values; create_garden_list() performs validation.
        self._prize_point = value

    def create(self) -> str:
        """Return a formatted string with prize points info added."""
        return super().create() + f", Prize points: {self.prize_point}"


# GardenManager demonstrates different method types:
# - instance methods: work on a specific GardenManager object
# - class methods: create or configure GardenManager objects
# - static methods: utility/statistics logic that needs no object state
class GardenManager:
    """Manages gardens grouped by manager name.
    Each manager name maps to a list of Plant objects. The report() method
    prints analytics for each garden."""

    # Nested class example:
    # GardenStats lives *inside* GardenManager because it only makes sense in
    # the context of garden management and statistics.
    class GardenStats:
        """Statistics helper (nested class)."""

        # Static method example:
        # @staticmethod is used when a method does NOT need access to self
        # (instance) or cls (class). It works like a grouped helper function
        # that logically belongs to this class.
        @staticmethod
        def plant_type_counts(garden):
            """Count how many trees, flowering plants, and prize flowers."""
            # Count plant types using isinstance to distinguish subclasses
            trees = 0
            flowers = 0
            prizes = 0

            for plant in garden:
                if isinstance(plant, Tree):
                    trees += 1
                elif isinstance(plant, PrizeFlower):
                    prizes += 1
                elif isinstance(plant, FloweringPlant):
                    flowers += 1

            return trees, flowers, prizes

        @staticmethod
        def total_growth(garden):
            """Calculate total growth for all plants in the garden."""
            total = 0.0
            for plant in garden:
                total += plant.growth()
            return total

        @staticmethod
        def validate(garden):
            """Check that all plants have valid (non-negative) heights and
            prize points."""
            # Validation happens on already-created objects (sanity check)
            for plant in garden:
                if plant.height < 0:
                    return False
                if isinstance(plant, PrizeFlower) and plant.prize_point < 0:
                    return False
            return True

        @staticmethod
        def garden_score(garden):
            """Calculate a score based on counts of each plant type."""
            trees, flowers, prizes = (GardenManager.
                                      GardenStats.plant_type_counts(garden))
            return (trees * 50) + (flowers * 25) + (prizes * 100)

    def __init__(self) -> None:
        """Initialize an empty dictionary to hold gardens by manager."""
        self.gardens = {}

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the appropriate garden list by manager."""
        # First time this manager appears, create an empty garden list
        if plant.manager not in self.gardens:
            self.gardens[plant.manager] = []
        self.gardens[plant.manager].append(plant)

    def add_plants(self, plants) -> None:
        """Add multiple plants to each managers gardens."""
        for plant in plants:
            self.add_plant(plant)

    # Class method example:
    # @classmethod receives the class itself as 'cls'.
    # It is often used as an alternative constructor that builds and returns a
    # new object of the class.
    @classmethod
    def create_garden_manager(cls, plants) -> "GardenManager":
        """Create a GardenManager from a list of Plant objects."""
        manager = cls()
        manager.add_plants(plants)
        return manager

    def create_garden_report(self) -> None:
        """Print a detailed create_garden_report for each garden and overall
        scores."""
        print(f"{C.BLUE}=== Garden Management System ==={C.RESET}")
        stats = GardenManager.GardenStats
        # Loop once per manager (each manager owns one garden)
        for manager_name, garden in self.gardens.items():
            print("\nPlants are being processed...")
            for plant in garden:
                plant.plant_add()

            print(f"\n{C.GREEN}{manager_name}{C.RESET} "
                  f"is helping plants grow...")
            for plant in garden:
                plant.growth_display()

            print(f"\n{C.CYAN}=== {manager_name}'s Garden Report ==={C.RESET}")
            for plant in garden:
                print(plant.create())

            trees, flowers, prizes = stats.plant_type_counts(garden)

            print(f"\nPlants added: {len(garden)}")
            print(f"Total growth: {stats.total_growth(garden):.0f}cm")
            print(f"Plant types: {trees} trees, "
                  f"{flowers} flowering, {prizes} prize")

            print(f"Height validation: {stats.validate(garden)}")

        print(f"\n{C.BLUE}=== Garden Score ==={C.RESET}")
        for manager_name, garden in self.gardens.items():
            print(f"{C.GREEN}{manager_name}{C.RESET}: "
                  f"{stats.garden_score(garden)}")


def create_garden_list():
    """Create plants using error_list validation. Returns a list of validated
    Plant objects."""

    # Checklist tuples: (type, name, height_cm, manager, color, prize_points)
    plant_check_list = [
        ("FloweringPlant", "Rose", 35, "Alice", "red", None),
        ("PrizeFlower", "Tulip", 28, "Alice", "yellow", 2),
        ("PrizeFlower", "Lily", 40, "Bob", "white", 4),
        ("Tree", "Oak Tree", 500, "Alice", None, None),
        ("Tree", "Pine Tree", 420, "Kenny", None, None),
        ("Tree", "Maple Tree", 332, "Bob", None, None),
    ]

    garden = []

    # Each checklist entry is validated before any object is created
    for (class_type, name, height, manager, color,
         prize_point) in plant_check_list:

        # Collect all validation errors for this entry
        error_list = []
        print(f"\nCreating secure {C.YELLOW}{name}{C.RESET}...")

        if height < 0:
            error_list.append(f"Invalid operation attempted: height "
                              f"{height}cm {C.BG_RED}[REJECTED]{C.RESET}\n"
                              f"Security: Negative height rejected!")

        if (class_type == "PrizeFlower" and prize_point is not None
                and prize_point < 0):
            error_list.append(f"Invalid operation attempted: prize points "
                              f"{prize_point} {C.BG_RED}[REJECTED]{C.RESET}\n"
                              f"Security: Negative prize points rejected!")

        # If any errors were found, reject creation and move on
        if error_list:
            print(f"{C.BG_RED}Error{C.RESET} during creation of {name} :(")
            for error in error_list:
                print(error)
            continue

        # Object creation happens only when input is considered safe
        if class_type == "Tree":
            garden.append(Tree(name, height, manager))
        elif class_type == "FloweringPlant":
            garden.append(FloweringPlant(name, height, manager, str(color)))
        elif class_type == "PrizeFlower":
            garden.append(PrizeFlower(name, height, manager, str(color),
                                      int(prize_point)))
    return garden


def main():
    """Main function to create gardens, build manager, and print reports."""
    # Build a list of validated Plant objects
    garden = create_garden_list()

    # Group plants into gardens by manager name
    manager = GardenManager.create_garden_manager(garden)

    # Display reports and scores
    manager.create_garden_report()


if __name__ == "__main__":
    main()
