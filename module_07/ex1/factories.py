#!/usr/bin/env python3


"""Factory classes used to create ex1 creature families."""


from ex0 import factories
from ex0.creatures import Creature
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(factories.CreatureFactory):
    """Factory used to create healing creature family members."""

    def create_base(self) -> Creature:
        """Return the base healing creature."""
        # Create the base form of the healing creature family.
        return Sproutling()

    def create_evolved(self) -> Creature:
        """Return the evolved healing creature."""
        # Create the evolved form of the healing creature family.
        return Bloomelle()


class TransformCreatureFactory(factories.CreatureFactory):
    """Factory used to create transforming creature family members."""

    def create_base(self) -> Creature:
        """Return the base transforming creature."""
        # Create the base form of the transforming creature family.
        return Shiftling()

    def create_evolved(self) -> Creature:
        """Return the evolved transforming creature."""
        # Create the evolved form of the transforming creature family.
        return Morphagon()
