#!/usr/bin/env python3

"""
Provide potion brewing functions for the alchemy package.

This module combines elemental functions from both package and root-level
modules to create potion recipes.

The module demonstrates how multiple import styles can be used inside the same
file.
"""


# Import elemental functions from the alchemy package.
import alchemy.elements
# Import elemental functions from the root-level module.
import elements


def healing_potion() -> str:
    """Create and return the healing potion recipe."""
    # Combine elemental functions to build the healing potion.
    return (f"Healing potion brewed with '{alchemy.elements.create_earth()}' "
            f"and '{alchemy.elements.create_air()}'")


def strength_potion() -> str:
    """Create and return the strength potion recipe."""
    # Combine elemental functions to build the strength potion.
    return (f"Strength potion brewed with '{elements.create_fire()}' "
            f"and '{elements.create_water()}'")
