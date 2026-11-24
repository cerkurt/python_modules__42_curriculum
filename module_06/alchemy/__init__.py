"""
Initialize the main alchemy package.

This package exposes selected elemental, potion, and transmutation functions
through a simplified public interface.

The `__all__` variable defines which objects are publicly available when
importing the alchemy package.
"""

# Expose selected elemental and potion functions.
from .elements import create_air
from .potions import strength_potion
from .potions import healing_potion as heal
# Expose nested package modules through the alchemy interface.
from . import transmutation

# Define the public objects available from the alchemy package.
__all__ = ["create_air", "strength_potion", "heal", "transmutation"]
