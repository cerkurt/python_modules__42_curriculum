#!/usr/bin/env python3


"""
Practice lambda expressions and small functional-programming tools.

This exercise is about treating functions as values.
In Python, a function is not only a block of code that can be called.
A function can also be stored in a variable, passed to another function,
returned from another function, and used s a small rule for sorting, filtering,
transforming, or calculating data.

Important terms for this module:
- Lambda expression:
  A lambda is a small anonymous function. "Anonymous" means it has no normal
  function name like a function created with def. Lambdas are useful when the
  function is short, simple, and only needed in one place.
    Example idea:
      lambda mage: mage["power"]
    This means: "receive one mage dictionary and return its power value".

- Higher-order function:
  A higher-order function is a function that works with another function. In
  this file, sorted(), filter(), map(), max(), and min() are used as
  higher-order functions because they receive lambda functions as arguments.

- key argument:
  In sorted(), max(), and min(), the key argument receives a function. That
  function tells Python which value should be used for comparison. For example,
  sorting artifact dictionaries by power requires a key function because Python
  should compare artifact["power"], not the whole dictionary.

- map():
  map() applies a function to every item in an iterable and produces
  transformed values. In this exercise, it is used to transform spell names.

- filter():
  filter() applies a condition function to every item in an iterable and keeps
  only the items where the condition returns True. In this exercise, it is used
  to keep only mages whose power is high enough.

- list(...):
  map() and filter() return lazy iterable objects. Wrapping them with list()
  makes the final result visible and returns a normal list.

The goal is not only to make the functions work, but also to understand where
small lambda functions are useful and how they are passed into other functions.
"""


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Return artifacts sorted by power from highest to lowest.
    The input is a list of dictionaries. Each dictionary represents one
    artifact and is expected to contain a "power" key.

    sorted() needs to know how to compare the dictionaries. The key argument
    provides that rule. The lambda receives one artifact at a time and returns
    artifact["power"]. Python then sorts by those returned power values.

    reverse=True means descending order, so the strongest artifact comes first.
    The original list is not changed; sorted() returns a new list.
    """

    # Take one artifact and use its power value for sorting.
    return sorted(
        artifacts, key=(lambda artifact: artifact["power"]), reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Return mages whose power is greater than or equal to min_power.

    filter() receives two arguments: a condition function and an iterable. The
    condition function must return True or False for each item.

    The lambda receives one mage dictionary at a time. If mage["power"] is at
    least min_power, the lambda returns True and filter() keeps that mage.
    Otherwise, the mage is skipped.

    list() is used because filter() returns a lazy filter object, not a normal
    list immediately.
    """

    # for mage in mages:
    #   if mage["power"] >= min_power:
    #     filter this mage
    return list(filter((lambda mage: mage["power"] >= min_power), mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Return spell names surrounded by magical star markers.

    map() receives a transformation function and an iterable. It applies the
    function to each item and produces the transformed values.

    The lambda receives one spell name at a time and returns a new formatted
    string. For example, "fireball" becomes "* fireball *".

    This is a transformation, not a filter: every input spell produces one
    output spell string.
    """

    # For each spell name, create a new string with asterics around it.
    # for spell in spells:
    #   make "* spell *"
    return list(map((lambda spell: f"* {spell} *"), spells))


def mage_stats(mages: list[dict]) -> dict:
    """Return maximum, minimum, and average mage power.

    max() and min() also support the key argument. Just like with sorted(), the
    key lambda tells Python which value should be used for comparison.

    max_mage stores the whole mage dictionary with the highest power, notonly
    the power number. min_mage stores the whole dictionary with the lowest
    power.

    For the average, map() extracts only the power values from all mage
    dictionaries. sum() adds those powers, len(mages) gives the number of
    mages, and round(..., 2) keeps the result readable with two decimal places.
    """

    max_mage = max(mages, key=(lambda mage: mage["power"]))

    # For each mage, look at mage["power"] when deciding which one is the
    # maximum.
    max_mage = max(mages, key=(lambda mage: mage["power"]))

    # For each mage, look at mage["power"] when deciding which one is the
    # minimum.
    min_mage = min(mages, key=(lambda mage: mage["power"]))
    avg_power = round(
        sum(map((lambda mage: mage["power"]), mages)) / len(mages), 2
    )
    return {
        "max_power": max_mage["power"],
        "min_power": min_mage["power"],
        "avg_power": avg_power,
    }


def main() -> None:
    print(f"{C.BLUE}Testing artifact sorter...{C.RESET}")
    artifacts = [
        {'name': 'Lightning Rod', 'power': 67, 'type': 'relic'},
        {'name': 'Wind Cloak', 'power': 116, 'type': 'accessory'},
        {'name': 'Shadow Blade', 'power': 70, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 91, 'type': 'relic'}
        ]

    try:
        # The sorter returns a new list ordered from strongest to weakest.
        sorted_artifacts = artifact_sorter(artifacts)

        # Print neighboring pairs so the sorted order is easy to inspect.
        for index in range(len(sorted_artifacts) - 1):
            current_artifact = sorted_artifacts[index]
            next_artifact = sorted_artifacts[index + 1]

            print(
                f"{C.YELLOW}{current_artifact['name']} "
                f"({current_artifact['power']} power){C.RESET} comes before "
                f"{C.YELLOW}{next_artifact['name']} "
                f"({next_artifact['power']} power){C.RESET}"
            )
    except Exception as error:
        print(f"{C.BG_RED}Caught an Exception:{C.RESET} "
              f"{C.RED}({type(error).__name__}){C.RESET} {error}")

    print(f"{C.BLUE}\nTesting power filter...{C.RESET}")
    mages = [
        {'name': 'Morgan', 'power': 67, 'element': 'fire'},
        {'name': 'Rowan', 'power': 80, 'element': 'light'},
        {'name': 'Casey', 'power': 98, 'element': 'fire'},
        {'name': 'Ember', 'power': 54, 'element': 'ice'},
        {'name': 'Riley', 'power': 84, 'element': 'lightning'}
        ]

    try:
        # Keep only mages whose power is at least 70.
        filtered_power = power_filter(mages, 70)
        for mage in filtered_power:
            print(f"{mage['name']} ({mage['power']} power)")
    except Exception as error:
        print(f"{C.BG_RED}Caught an Exception:{C.RESET} "
              f"{C.RED}({type(error).__name__}){C.RESET} {error}")

    print(f"{C.BLUE}\nTesting spell transformator...{C.RESET}")
    spells = [
        'fireball',
        'tornado',
        'heal',
        'freeze'
        ]

    try:
        # Transform each spell name, then join the list for one-line output.
        transformed_spells = spell_transformer(spells)
        print(" ".join(transformed_spells))
    except Exception as error:
        print(f"{C.BG_RED}Caught an Exception:{C.RESET} "
              f"{C.RED}({type(error).__name__}){C.RESET} {error}")

    print(f"{C.BLUE}\nTesting stats analyzer...{C.RESET}")
    try:
        # Calculate summary statistics from the same mage data.
        stats = mage_stats(mages)
        print(stats)
    except Exception as error:
        print(f"{C.BG_RED}Caught an Exception:{C.RESET} "
              f"{C.RED}({type(error).__name__}){C.RESET} {error}")


if __name__ == "__main__":
    main()
