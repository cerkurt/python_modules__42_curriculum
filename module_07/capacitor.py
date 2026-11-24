#!/usr/bin/env python3


"""Test script used to demonstrate the ex1 creature capabilities."""


import ex1


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


def factory_tester() -> None:
    """Create creatures with capabilities and display their actions."""
    # Create factory objects for both special creature families.
    heal = ex1.HealingCreatureFactory()
    transform = ex1.TransformCreatureFactory()

    # Create both base and evolved creature forms.
    creature_1 = heal.create_base()
    creature_2 = transform.create_base()

    evolve_1 = heal.create_evolved()
    evolve_2 = transform.create_evolved()

    # Display the healing creature family actions.
    if (isinstance(creature_1, ex1.capabilities.HealCapability)
        and
            isinstance(evolve_1, ex1.capabilities.HealCapability)):
        print(
            f"{C.YELLOW}Testing Creature with healing "
            f"capability...\n\n{C.RESET}"
            f"{C.YELLOW}\nBase Class\n{C.RESET}"
            f"{creature_1.describe()}\n"
            f"{creature_1.attack()}!\n"
            f"{creature_1.heal()}!\n"
            f"{C.YELLOW}\nEvolved Class\n{C.RESET}"
            f"{evolve_1.describe()}\n"
            f"{evolve_1.attack()}!\n"
            f"{evolve_1.heal()}!\n"
            )

    # Display the transforming creature family actions.
    if (isinstance(creature_2, ex1.capabilities.TransformCapability)
        and
            isinstance(evolve_2, ex1.capabilities.TransformCapability)):
        print(
            f"{C.YELLOW}Testing Creature with transform "
            f"capability...\n\n{C.RESET}"
            f"{C.YELLOW}\nBase Class\n{C.RESET}"
            f"{creature_2.describe()}\n"
            f"{creature_2.attack()}!\n"
            f"{creature_2.transform()}!\n"
            f"{creature_2.revert()}\n"
            f"{C.YELLOW}\nEvolved Class\n{C.RESET}"
            f"{evolve_2.describe()}\n"
            f"{evolve_2.attack()}\n"
            f"{evolve_2.transform()}!\n"

            # Attack again after transformation to show the state change.
            f"{evolve_2.attack()}!\n"
            f"{evolve_2.revert()}\n"
            )


if __name__ == "__main__":
    factory_tester()
