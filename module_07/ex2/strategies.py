#!/usr/bin/env python3


"""Battle strategy classes used to control creature actions in ex2."""


from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability
from abc import ABC, abstractmethod


class StrategyError(Exception):
    """Custom exception raised for invalid strategy usage."""
    pass


class BattleStrategy(ABC):
    """Abstract base class used by all battle strategies."""

    @abstractmethod
    def is_valid(self, creature_obj: Creature) -> bool:
        """Check whether the strategy can be used with the creature."""
        pass

    @abstractmethod
    def act(self, creature_obj: Creature) -> str:
        """Perform the strategy actions for the creature."""
        pass


class NormalStrategy(BattleStrategy):
    """Basic strategy that performs only a normal attack."""

    def is_valid(self, creature_obj: Creature) -> bool:
        """Allow all creature types to use this strategy."""
        return True

    def act(self, creature_obj: Creature) -> str:
        """Return the normal attack action of the creature."""
        return creature_obj.attack()


class AggressiveStrategy(BattleStrategy):
    """Strategy focused on transformation and strong attacks."""

    def is_valid(self, creature_obj: Creature) -> bool:
        """Allow only transforming creatures to use this strategy."""
        return isinstance(creature_obj, TransformCapability)

    def act(self, creature_obj: Creature) -> str:
        """Perform transform, attack, and revert actions in order."""
        if not isinstance(creature_obj, TransformCapability):
            raise StrategyError("Invalid creature "
                                "for aggressive strategy")

        # Execute the full aggressive action sequence.
        transform_ability = creature_obj.transform()
        attack_ability = creature_obj.attack()
        revert_ability = creature_obj.revert()

        return (
            f"{transform_ability}\n"
            f"{attack_ability}\n"
            f"{revert_ability}"
                )


class DefensiveStrategy(BattleStrategy):
    """Strategy focused on attacking and healing."""

    def is_valid(self, creature_obj: Creature) -> bool:
        """Allow only healing creatures to use this strategy."""
        return isinstance(creature_obj, HealCapability)

    def act(self, creature_obj: Creature) -> str:
        """Perform attack and healing actions in order."""
        if not isinstance(creature_obj, HealCapability):
            raise StrategyError("Invalid creature "
                                "for defensive strategy")

        # Execute the defensive action sequence.
        attack_ability = creature_obj.attack()
        heal_ability = creature_obj.heal()

        return (
            f"{attack_ability}\n"
            f"{heal_ability}"
                )
