#!/usr/bin/env python3


"""
Validate ingredients used for light magic spells.

This module checks whether spell ingredients contain at least one allowed light
ingredient from the light spellbook.

The light magic implementation avoids circular imports by using safe import
organization between modules.
"""


# Import allowed ingredients from the light spellbook module.
from alchemy.grimoire import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    """Check whether the provided ingredients are valid for light magic."""
    # Retrieve the list of ingredients allowed for light spells.
    allowed_ing = light_spellbook.light_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()
    # Validate ingredients using a case-insensitive comparison.
    for item in allowed_ing:
        if item in lower_ingredients:
            return "VALID"
    return "INVALID"
