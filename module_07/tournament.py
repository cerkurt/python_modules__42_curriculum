#!/usr/bin/env python3


"""Test script used to run ex2 creature tournaments with strategies."""


from ex0.factories import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (BattleStrategy,
                            NormalStrategy,
                            DefensiveStrategy,
                            AggressiveStrategy)
from ex2.strategies import StrategyError


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


def opponent_info(
        tournament_round: int
        ) -> list[tuple[CreatureFactory, BattleStrategy]]:
    """Return the factory and strategy pairs for one tournament."""
    # Each tuple contains one factory and the strategy used by its creature.
    if tournament_round == 0:
        return [(FlameFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())]
    elif tournament_round == 1:
        return [(FlameFactory(), AggressiveStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())]
    elif tournament_round == 2:
        return [(AquaFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy()),
                (TransformCreatureFactory(), AggressiveStrategy())]
    else:
        raise ValueError("Invalid tournament number. Should be between 0-2")


def factory_tag(factory: CreatureFactory) -> str:
    """Return a readable label for a creature factory."""
    if isinstance(factory, FlameFactory):
        return "Flameling"
    elif isinstance(factory, AquaFactory):
        return "Aquabub"
    elif isinstance(factory, HealingCreatureFactory):
        return "Healing"
    elif isinstance(factory, TransformCreatureFactory):
        return "Transform"
    return f"{C.RED}Unknown factory tag{C.RESET}"


def strategy_tag(strategy: BattleStrategy) -> str:
    """Return a readable label for a battle strategy."""
    if isinstance(strategy, NormalStrategy):
        return "Normal"
    elif isinstance(strategy, AggressiveStrategy):
        return "Aggressive"
    elif isinstance(strategy, DefensiveStrategy):
        return "Defensive"
    return f"{C.RED}Unknown strategy tag{C.RESET}"


def info_formatting(
        opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> str:
    """Format the opponent list for display before a tournament."""
    formatted_string = []

    # Build labels such as "(Flameling + Normal)" for each opponent.
    for factory, strategy in opponents:
        string = f"({factory_tag(factory)} + {strategy_tag(strategy)})"
        formatted_string.append(string)

    return "[" + ", ".join(formatted_string) + "]"


def tournament_info(
        tournament_round: int,
        opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    """Print the title and basic information for one tournament."""

    if tournament_round == 0:
        print(f"{C.BLUE}Tournament {tournament_round} (basic){C.RESET}\n"
              f"{info_formatting(opponents)}\n"
              f"{C.YELLOW}*** Tournament ***{C.RESET}\n"
              f"{len(opponents)} opponents involded")

    elif tournament_round == 1:
        print(f"{C.BLUE}Tournament {tournament_round} (error){C.RESET}\n"
              f"{info_formatting(opponents)}\n"
              f"{C.YELLOW}*** Tournament ***{C.RESET}\n"
              f"{len(opponents)} opponents involded")

    elif tournament_round == 2:
        print(f"{C.BLUE}Tournament {tournament_round} (multiple){C.RESET}\n"
              f"{info_formatting(opponents)}\n"
              f"{C.YELLOW}*** Tournament ***{C.RESET}\n"
              f"{len(opponents)} opponents involded")

    else:
        if tournament_round < 0 or tournament_round > 2:
            raise ValueError(
                "Invalid tournament number. Should be between 0-2")

        else:
            raise TypeError(
                "Object type does not match with the requirement.")


def battle_info(
        opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    """Make each opponent battle every other opponent once."""

    # Use index pairs so each matchup happens only once.
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]

            # The example tournament uses base creatures from each factory.
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print(f"{C.YELLOW}\n* Battle *{C.RESET}")
            print(creature_a.describe())
            print("  vs.")
            print(creature_b.describe())
            print("  now fight!\n")

            # Strategies decide how each creature acts during battle.
            try:
                print(strategy_a.act(creature_a))
                print(strategy_b.act(creature_b))
            except StrategyError as error:
                print(f"{C.RED}Battle error, aborting tournament:{C.RESET} "
                      f"{C.BG_RED}{error}{C.RESET}")
                return


def main() -> None:
    """Run all tournament demo scenarios."""

    # Basic tournament with valid strategy combinations.
    opponents = opponent_info(0)
    tournament_info(0, opponents)
    print()
    battle_info(opponents)
    print()

    # Error tournament with an invalid aggressive strategy combination.
    opponents = opponent_info(1)
    tournament_info(1, opponents)
    print()
    battle_info(opponents)
    print()

    # Larger tournament with three different creature families.
    opponents = opponent_info(2)
    tournament_info(2, opponents)
    print()
    battle_info(opponents)
    print()


if __name__ == "__main__":
    main()
