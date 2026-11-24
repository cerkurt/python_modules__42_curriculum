"""
Initialize the transmutation package.

This package contains recipe modules responsible for advanced alchemy
transformations such as lead transmutation.

The package exposes selected modules through `__all__` to define its public
package interface.
"""

# Expose the recipes module through the transmutation package.
from . import recipes

# Define the public objects available from the transmutation package.
__all__ = ["recipes"]
