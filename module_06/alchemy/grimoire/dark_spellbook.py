#!/usr/bin/env python3


"""
Provide dark spellbook functions for forbidden magic.

This module stores allowed ingredients for dark spells and records spell
attempts after ingredient validation.

The module intentionally participates in a circular import with
`dark_validator.py` to demonstrate unsafe package dependencies.
"""


# Import validation functions from the dark validator module.
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    """Return the list of ingredients allowed for dark magic."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Validate ingredients and record the dark spell result."""
    # Validate the spell ingredients before recording the spell.
    decision = validate_ingredients(ingredients)
    if decision == "VALID":
        return f"Spell recorded: {spell_name} ({ingredients} - {decision})"
    else:
        return f"Spell rejected: {spell_name} ({ingredients} - {decision})"
