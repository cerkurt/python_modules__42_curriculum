#!/usr/bin/env python3


"""Base creature classes and concrete creature implementations for ex0."""


from abc import ABC, abstractmethod


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


class Creature(ABC):
    """Abstract base class used by all creature types."""

    def __init__(self, creature_name: str, creature_type: str) -> None:
        """Store the creature name and elemental type."""
        self.creature_name = creature_name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """Return the attack action of the creature."""
        pass

    def describe(self) -> str:
        """Return a short description of the creature."""
        # Apply different colors depending on the creature type.
        if self.creature_type == "Fire":
            return (f"{self.creature_name} is a "
                    f"{C.RED}{self.creature_type}{C.RESET} type Creature.")
        elif self.creature_type == "Water":
            return (f"{self.creature_name} is a "
                    f"{C.BLUE}{self.creature_type}{C.RESET} type Creature.")
        elif self.creature_type == "Fire / Flying":
            return (f"{self.creature_name} is a "
                    f"{C.RED}{self.creature_type}{C.RESET} type Creature.")
        elif self.creature_type == "Grass":
            return (f"{self.creature_name} is a "
                    f"{C.GREEN}{self.creature_type}{C.RESET} type Creature.")
        elif self.creature_type == "Grass / Fairy":
            return (f"{self.creature_name} is a "
                    f"{C.GREEN}{self.creature_type}{C.RESET} type Creature.")
        else:
            return (f"{self.creature_name} is a "
                    f"{C.PURPLE}{self.creature_type}{C.RESET} type Creature.")


class Flameling(Creature):
    """Base fire creature."""

    def __init__(self) -> None:
        # Initialize the creature with a fixed name and type.
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """Return Flameling's attack action."""
        return f"{self.creature_name} uses {C.RED}Ember{C.RESET}"


class Pyrodon(Creature):
    """Evolved fire creature."""

    def __init__(self) -> None:
        # Initialize the creature with a fixed name and type.
        super().__init__("Pyrodon", "Fire / Flying")

    def attack(self) -> str:
        """Return Pyrodon's attack action."""
        return f"{self.creature_name} uses {C.RED}Flamethrower{C.RESET}"


class Aquabub(Creature):
    """Base water creature."""

    def __init__(self) -> None:
        # Initialize the creature with a fixed name and type.
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """Return Aquabub's attack action."""
        return f"{self.creature_name} uses {C.BLUE}Water Gun{C.RESET}"


class Torragon(Creature):
    """Evolved water creature."""

    def __init__(self) -> None:
        # Initialize the creature with a fixed name and type.
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """Return Torragon's attack action."""
        return f"{self.creature_name} uses {C.BLUE}Hydro Pump{C.RESET}"
