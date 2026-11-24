#!/usr/bin/env python3
"""
This script demonstrates the concept of encapsulation.

It shows how a class can protect its internal data (height and age)
by allowing changes only through controlled setter methods that
validate input before storing it.
"""


class C:
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    BG_RED = "\033[41m"


class SecurePlant:
    """Represent a plant with protected attributes.

    Height and age are stored as private attributes and can only be modified
    through setter methods that enforce validation rules."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name

        # Private att: direct access from outside the class is discouraged
        self._height = 0
        self._age = 0

        print(f"\nPlant created: {C.YELLOW}{self.name}{C.RESET}")

        # Use setters so validation rules are applied at creation time
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """Return the stored height in centimeters."""
        return self._height

    def get_age(self) -> int:
        """Return the stored age in days."""
        return self._age

    def set_height(self, new_height: int) -> None:
        """Update the plant's height if the value is valid.

        Negative values are rejected to protect the object's state.
        """
        if new_height < 0:
            print(f"\nInvalid operation attempted: height {new_height}cm "
                  f"{C.BG_RED}[REJECTED]{C.RESET}\n"
                  f"Security: Negative age rejected!")
            return None

        self._height = new_height
        print(f"Height updated: {self._height}cm {C.GREEN}[OK]{C.RESET}")

    def set_age(self, new_age: int) -> None:
        """Update the plant's age if the value is valid.

        Negative values are rejected to protect the object's state.
        """
        if new_age < 0:
            print(f"\nInvalid operation attempted: age {new_age} days "
                  f"{C.BG_RED}[REJECTED]{C.RESET}\n"
                  f"Security: Negative age rejected!")
            return None

        self._age = new_age
        print(f"Age updated: {self._age} days {C.GREEN}[OK]{C.RESET}")

    def show(self) -> None:
        """Display the current, validated state of the plant."""
        print(f"\nCurrent plant: {C.YELLOW}{self.name}{C.RESET} "
              f"({self.get_height()}cm, {self.get_age()} days)")


def main() -> None:
    print(f"{C.BLUE}=== Garden Security System ==={C.RESET}")

    # Create several SecurePlant objects with initial values
    plant1 = SecurePlant("Rose", 25, 30)
    plant2 = SecurePlant("Oak", 350, 482)
    plant3 = SecurePlant("Daisy", 45, 31)

    garden = [plant1, plant2, plant3]

    # Attempt invalid updates to demonstrate rejection by setters
    for plant in garden:
        plant.set_height(-5)
        plant.set_age(-10)
        plant.show()
    return None


if __name__ == "__main__":
    main()
