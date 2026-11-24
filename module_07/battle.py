#!/usr/bin/env python3


"""Simple test script used to demonstrate the ex0 creature factories."""


import ex0


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"


def factory_tester() -> None:
    """Create creatures from factories and display their actions."""
    # Create factory objects for each creature family.
    flame = ex0.FlameFactory()
    water = ex0.AquaFactory()

    # Create both base and evolved creature forms.
    creature_1 = flame.create_base()
    creature_2 = water.create_base()

    evolve_1 = flame.create_evolved()
    evolve_2 = water.create_evolved()

    # Display the fire creature family.
    print(f"{C.YELLOW}Testing factory...{C.RESET}\n"
          f"{creature_1.describe()}\n{creature_1.attack()}!\n"
          f"{evolve_1.describe()}\n{evolve_1.attack()}!\n")

    # Display the water creature family.
    print(f"{C.YELLOW}Testing factory...{C.RESET}\n"
          f"{creature_2.describe()}\n{creature_2.attack()}!\n"
          f"{evolve_2.describe()}\n{evolve_2.attack()}!\n")

    # Simulate a simple battle between the base creatures.
    print(f"{C.YELLOW}Testing battle...{C.RESET}\n"
          f"{creature_1.describe()}\n vs\n{creature_2.describe()}\n fight!\n"
          f"{creature_1.attack()}!\n{creature_2.attack()}!")


if __name__ == "__main__":
    factory_tester()
