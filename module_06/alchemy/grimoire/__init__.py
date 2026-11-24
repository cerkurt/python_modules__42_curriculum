"""
Initialize the grimoire package.

This package contains spellbook and validation modules used for light and dark
magic demonstrations.

The package exports selected modules through `__all__` to control which objects
are exposed when importing the package.
"""

# Expose safe light magic modules through the package interface.
from . import light_spellbook
from . import light_validator

# Define the public objects available from the grimoire package.

__all__ = ["light_spellbook", "light_validator"]
