#!/usr/bin/env python3


"""Additional creature implementations with special capabilities for ex1."""


from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


class Sproutling(Creature, HealCapability):
    """Base grass creature with healing abilities."""
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        """Return Sproutling's attack action."""
        return f"{self.creature_name} uses {C.GREEN}Vine Whip{C.RESET}"

    def heal(self) -> str:
        """Return Sproutling's healing action."""
        return f"{self.creature_name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Evolved grass creature with stronger healing abilities."""
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass / Fairy")

    def attack(self) -> str:
        """Return Bloomelle's attack action."""
        return f"{self.creature_name} uses {C.GREEN}Petal Dance{C.RESET}"

    def heal(self) -> str:
        """Return Bloomelle's healing action."""
        return (
            f"{self.creature_name} heals itself and others for a large amount"
            )


class Shiftling(Creature, TransformCapability):
    """Base transforming creature."""
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        # Store whether the creature is currently transformed.
        self.transform_state = False

    def attack(self) -> str:
        """Return a different attack depending on the transform state."""
        # Use a stronger attack after transformation.
        if self.transform_state is False:
            return f"{self.creature_name} attacks normally."
        else:
            return (f"{self.creature_name} performs a "
                    f"{C.PURPLE}boosted strike{C.RESET}")

    def transform(self) -> str:
        """Enable the transformed battle state."""
        self.transform_state = True
        return (
            f"{self.creature_name} {C.PURPLE}shifts{C.RESET} "
            f"into a sharper form"
            )

    def revert(self) -> str:
        """Return the creature to its normal state."""
        self.transform_state = False
        return f"{self.creature_name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """Evolved transforming creature with stronger attacks."""
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal / Dragon")
        # Store whether the creature is currently transformed.
        self.transform_state = False

    def attack(self) -> str:
        """Return a different attack depending on the transform state."""
        # Use a stronger attack after transformation.
        if self.transform_state is False:
            return f"{self.creature_name} attacks normally."
        else:
            return (f"{self.creature_name} unleashes a "
                    f"{C.PURPLE}devastating morph strike{C.RESET}")

    def transform(self) -> str:
        """Enable the transformed battle state."""
        self.transform_state = True
        return (f"{self.creature_name} {C.PURPLE}morphs{C.RESET} into "
                f"dragonic battle form!")

    def revert(self) -> str:
        """Return the creature to its normal state."""
        self.transform_state = False
        return f"{self.creature_name} stabilizes its form."
