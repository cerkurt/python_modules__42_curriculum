#!/usr/bin/env python3


"""
Provide spellbook functions for light magic.

This module stores allowed ingredients for light spells and records spell
attempts after ingredient validation.

The light magic implementation avoids circular imports by using safe import
organization between modules.
"""


# Import validation functions from the light validator module.
from alchemy.grimoire import light_validator


def light_spell_allowed_ingredients() -> list:
    """Return the list of ingredients allowed for light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Validate ingredients and record the light spell result."""
    # Validate the spell ingredients before recording the spell.
    decision = light_validator.validate_ingredients(ingredients)
    if decision == "VALID":
        return f"Spell recorded: {spell_name} ({ingredients} - {decision})"
    else:
        return f"Spell rejected: {spell_name} ({ingredients} - {decision})"
