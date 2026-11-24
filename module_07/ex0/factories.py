#!/usr/bin/env python3


"""Factory classes used to create creature families for ex0."""


from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon
from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    """Abstract factory used to create base and evolved creatures."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create and return the base creature of the family."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create and return the evolved creature of the family."""
        pass


class FlameFactory(CreatureFactory):
    """Factory used to create fire creature family members."""

    def create_base(self) -> Creature:
        """Return the base fire creature."""
        # Create the base form of the fire creature family.
        return Flameling()

    def create_evolved(self) -> Creature:
        """Return the evolved fire creature."""
        # Create the evolved form of the fire creature family.
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory used to create water creature family members."""

    def create_base(self) -> Creature:
        """Return the base water creature."""
        # Create the base form of the water creature family.
        return Aquabub()

    def create_evolved(self) -> Creature:
        """Return the evolved water creature."""
        # Create the evolved form of the water creature family.
        return Torragon()
