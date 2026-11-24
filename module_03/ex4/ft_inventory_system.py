#!/usr/bin/env python3

"""
This module demonstrates dictionary fundamentals in a game-themed inventory:
- Parsing key:value pairs from command-line arguments (sys.argv)
- Validating input and raising clear exceptions on bad data
- Summarizing totals, percentages, and basic statistics from a dict[str, int]
- Using dictionary comprehensions/iteration patterns to build filtered views

The program prints multiple sections:
Inventory analysis, item details with percentages, most/least abundant items,
category grouping, restock suggestions, and dictionary properties.
"""

from enum import Enum
import sys


class C(str, Enum):
    """ANSI color codes used to make terminal output easier to read."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    BG_RED = "\033[41m"

    def __str__(self) -> str:
        return self.value


def parse_agruments() -> dict[str, int]:
    """Parse the arguments from sys.argv and return them as dictionary mapped
    as item_name -> quantity."""
    if len(sys.argv) == 1:
        raise ValueError(
            f"Please provide at least 1 inventory item(s) with value(s) to be "
            f"stored.\n{C.YELLOW}Example usage: python3 {sys.argv[0]} "
            f"<item1:value1> <item2:value2> <item3:value3> ...{C.RESET}"
            )

    player_inventory: dict[str, int] = {}

    # Parse each <item:amount> argument and update the inventory totals
    for argument in sys.argv[1:]:
        if ":" not in argument:
            raise ValueError("Please seperate item(s) and value(s) with : "
                             "between.\nExpected format: <item:value>")

        # Split only on the first ':' so item names can contain additional
        # ':' safely
        item_arg, amount_arg = argument.split(":", 1)
        if not item_arg:
            raise NameError(f"Invalid item name in '{argument}'. "
                            f"Item name cannot be empty.")

        if item_arg.isdigit():
            raise NameError(f"Invalid item name in '{argument}'. "
                            f"Item name cannot be only digits.")

        if not item_arg.isprintable():
            raise NameError(f"Invalid item name in '{argument}'. "
                            f"Item name must be printable.")

        for letter in item_arg:
            if not letter.isprintable():
                raise NameError(
                    f"Invalid item name in '{argument}'. Item "
                    f"name must contain only printable characters."
                    )
        # Convert the quantity to int (raise a clear error if conversion fails)
        try:
            dict_quantity = int(amount_arg)
        except ValueError:
            raise ValueError(f"Value for {argument} must be an integer value")

        if dict_quantity < 0:
            raise ValueError("Item value must be 0 or a positive integer.")
        # If an item appears multiple times, sum quantities instead of
        # overwriting
        if item_arg in player_inventory:
            player_inventory[item_arg] = (player_inventory[item_arg] +
                                          dict_quantity)
        else:
            player_inventory[item_arg] = dict_quantity

    return player_inventory


def inventory_system_analysis(inventory: dict[str, int]) -> None:
    """Prints the amount of keys and the sum of the values of the dictionary
    passed as parameter."""
    keys = list(inventory.keys())
    values = sum(inventory.values())
    print(f"{C.YELLOW}Total items in inventory:{C.RESET} "
          f"{values}\n"
          f"{C.YELLOW}Unique item types:{C.RESET} {len(keys)}")


def inventory_details(inventory: dict[str, int]) -> None:
    """Prints each item with its count and percentage of the total items. """
    values = sum(inventory.values())
    for item, value in inventory.items():
        print(f"{C.YELLOW}{item}:{C.RESET} {value} units "
              f"({round(((value * 100) / values), 2)}%)")


def inventory_statistics(inventory: dict[str, int]) -> None:
    """Prints the items with most and least occurance in the given
    arguments."""

    def most_abundant(inventory: dict[str, int]) -> tuple[str, int]:
        """Returns a tuple with the most occured item and its count. """
        max_value = 0
        for item, value in inventory.items():
            if value > max_value:
                max_value = value
                key_pair = item
        return (key_pair, max_value)

    def least_abundant(inventory: dict[str, int]) -> tuple[str, int]:
        """Returns a tuple with the least occured item and its count. """
        min_value = float('inf')
        for item, value in inventory.items():
            if value < min_value:
                min_value = value
                key_pair = item
        return (key_pair, min_value)

    type_max, amount_max = most_abundant(inventory)
    print(
        f"{C.YELLOW}Most abundant:{C.RESET} {type_max} ({amount_max} units)"
        )

    type_min, amount_min = least_abundant(inventory)
    print(
        f"{C.YELLOW}Least abundant:{C.RESET} {type_min} ({amount_min} units)\n"
        )


def item_categories(inventory: dict[str, int]) -> None:
    """Customly hardcoded item category check. As preference, if item name is
    potion, bread, apple or antidote, tag them as moderate. If item name is
    sword, helmet, axe, or gloves then tagged as rare/scarce items.

    Items are added to new dictionaries to be printed seperately."""
    moderate_items = {}
    for item, value in inventory.items():
        if (item == "potion" or
                item == "bread" or
                item == "apple" or
                item == "antidote"):
            moderate_items[item] = value
    print(f"{C.YELLOW}Moderate:{C.RESET} {moderate_items}")

    rare_items = {}
    for item, value in inventory.items():
        if (item == "sword" or
                item == "helmet" or
                item == "axe" or
                item == "gloves"):
            rare_items[item] = value
    print(f"{C.YELLOW}Scarce:{C.RESET} {rare_items}")


def stock_check(inventory: dict[str, int]) -> None:
    """If the amount of the item passed from CLI is lower than 3, item is added
    to a low_stock list and printed as stock is needed to stdout."""
    low_stock = {}
    for item, value in inventory.items():
        if value < 3:
            low_stock[item] = value
    print(f"{C.YELLOW}Restock Needed:{C.RESET} {list(low_stock)}")


def dictionary_properties_demo(inventory: dict[str, int]) -> None:
    """Function that prints keys and the values of the dictionary passed as
    argument.
    For randomly picked name (here it is sword), functions performs a lookup
    demo internally and prints the bool return."""
    print(f"{C.YELLOW}Dictionary Keys:{C.RESET} {list(inventory.keys())}\n"
          f"{C.YELLOW}Dictionary Values:{C.RESET} {list(inventory.values())}\n"
          f" ")

    def lookup_check(inventory: dict[str, int]) -> bool:
        """Does the look-up check internally for item name "sword". if yes,
        sword name is added to a check_list dict to be return as true or false
        based on the check_list lenght."""
        check_list = []
        for name in inventory.keys():
            if name == "sword":
                check_list.append(name)
        if len(check_list) == 0:
            return False
        else:
            return True

    sample_demo = lookup_check(inventory)
    if sample_demo:
        print(f"{C.YELLOW}Sample lookup - 'sword' in Inventory:{C.RESET} "
              f"{C.GREEN}{sample_demo}{C.RESET}")
    else:
        print(f"{C.YELLOW}Sample lookup - 'sword' in Inventory:{C.RESET} "
              f"{C.RED}{sample_demo}{C.RESET}")


def main() -> None:
    """Main is kept clean by only calling the necessary functions defined
    above."""
    user_inventory = parse_agruments()

    print(f"{C.BLUE}=== Inventory System Analysis ==={C.RESET}")
    inventory_system_analysis(user_inventory)

    print(f"{C.BLUE}\n=== Current Inventory ==={C.RESET}")
    inventory_details(user_inventory)

    print(f"{C.BLUE}\n=== Inventory Statistics ==={C.RESET}")
    inventory_statistics(user_inventory)

    print(f"{C.BLUE}\n=== Item Categories ==={C.RESET}")
    item_categories(user_inventory)

    print(f"{C.BLUE}\n=== Management Suggestions ==={C.RESET}")
    stock_check(user_inventory)

    print(f"{C.BLUE}\n=== Dictionary Properties Demo ==={C.RESET}")
    dictionary_properties_demo(user_inventory)


if __name__ == "__main__":
    # Catch any uncaught errors and display a consistent error header
    try:
        main()
    except Exception as error:
        print(f"{C.BG_RED}Error:{C.RESET} "
              f"{C.RED}{type(error).__name__}{C.RESET} {error}")
