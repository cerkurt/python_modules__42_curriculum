"""Public exports for the ex0 creature factory package."""


# Expose the public factory classes of the package.
from ex0.factories import FlameFactory, AquaFactory

# Limit what gets imported with `from ex0 import *`.
__all__ = ["FlameFactory", "AquaFactory"]
