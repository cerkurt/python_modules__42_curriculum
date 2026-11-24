"""Public exports for the ex2 battle strategy package."""


# Expose the public strategy classes and custom exception.
from .strategies import (
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    StrategyError,
)

# Limit what gets imported with `from ex2 import *`.
__all__ = [
    "NormalStrategy",
    "DefensiveStrategy",
    "AggressiveStrategy",
    "StrategyError",
]
