#!/usr/bin/env python3


"""
Provide advanced transmutation recipes for the alchemy package.

This module defines recipes used for complex alchemy operations, such as
transforming lead into gold.

The module demonstrates both relative and absolute imports inside nested
package structures.
"""


# Import elemental functions from nearby package modules.
from ..elements import create_air
from alchemy.potions import strength_potion
# Import functions from the root-level elements module.
import elements


def lead_to_gold() -> str:
    """Create the recipe used to transmute lead into gold."""
    # Combine elements and potions to build the transmutation recipe.
    return (f"Recipe transmuting Lead to Gold: "
            f"brew '{create_air()}' and "
            f"'{strength_potion()}' "
            f"mixed with '{elements.create_fire()}'")
