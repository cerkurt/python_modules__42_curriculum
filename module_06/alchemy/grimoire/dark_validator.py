#!/usr/bin/env python3


"""
Validate ingredients used for dark magic spells.

This module checks whether spell ingredients contain at least one allowed dark
ingredient from the dark spellbook.

The module intentionally participates in a circular import with
`dark_spellbook.py` to demonstrate unsafe package dependencies.
"""


# Import allowed ingredients from the dark spellbook module.
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Check whether the provided ingredients are valid for dark magic."""
    # Retrieve the list of ingredients allowed for dark spells.
    allowed_ing = dark_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()
    # Validate ingredients using a case-insensitive comparison.
    for item in allowed_ing:
        if item in lower_ingredients:
            return "VALID"
    return "INVALID"
