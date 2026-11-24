#!/usr/bin/env python3

"""
Practice useful tools from functools: reduce, partial, lru_cache, and
singledispatch.

This exercise continues the idea that functions are values. The functools
module contains ready-made tools for common function-related patterns. Instead
of manually writing every loop, wrapper, or dispatcher, we can use these
helpers to combine values, pre-fill function arguments, cache expensive
results, or choose behavior based on input type.

Important terms for this module:

- functools.reduce:
  reduce() combines many values into one final value. It receives a function
  that accepts two arguments, then repeatedly applies that function across the
  list. For example, reduce(operator.add, [10, 20, 30]) behaves like:
      10 + 20 = 30
      30 + 30 = 60
  The final result is 60.

- operator module:
  The operator module provides function versions of common operators. For
  example, operator.add is a function version of +, and operator.mul is a
  function version of *. This makes them useful with reduce().

- functools.partial:
  partial() creates a new callable by pre-filling some arguments of an existing
  function. The first argument passed to partial() is the original function.
  Everything after that is treated as already-filled arguments for the original
  function.

  Example idea:
      partial(base_enchantment, 50, "fire")

  This creates a new function that already knows power=50 and element="fire".
  The returned function still waits for the remaining argument, target.

- functools.lru_cache:
  lru_cache remembers previous function results. LRU means "least recently
  used". If the cache becomes full, the least recently used result can be
  removed. It is especially useful for recursive functions like Fibonacci,
  because the same smaller values are requested many times.

- cache_info():
  A cached function gets a cache_info() method. It shows hits, misses, maxsize,
  and currsize. Hits mean cached results were reused. Misses mean the function
  had to calculate the result.

- functools.singledispatch:
  singledispatch lets one function name behave differently depending on the
  type of its first argument. It is similar to type-based routing. In this
  exercise, int, str, and list inputs are handled by different registered
  functions.
"""

from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any

import operator
import random


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


class TestVariables:
    """Local test data for partial and dispatcher demonstrations."""

    ENCHANTMENT_TYPES = [
        "Flaming",
        "Frozen",
        "Shocking",
        "Earthen",
        "Windy",
        "Flowing",
        "Radiant",
        "Dark"]

    ENCHANTMENT_ITEMS = [
        "Sword",
        "Shield",
        "Staff",
        "Wand",
        "Armor",
        "Ring",
        "Amulet",
        "Cloak"]

    POWER_VALUES = [24, 14, 24]


class AncientLibrary:
    """Collection of static methods that demonstrate functools utilities.

    These methods do not use object state, so they are static methods. They are
    grouped in this class only to keep the exercise organized.
    """

    @staticmethod
    def spell_reducer(spells: list[int], operation: str) -> int:
        """Combine a list of spell powers into one value using reduce().

        spells is expected to be a list of integers. operation selects which
        two-argument function reduce() should use:

        - "add" uses operator.add to sum all values.
        - "multiply" uses operator.mul to multiply all values.
        - "max" uses the built-in max function pair by pair.
        - "min" uses the built-in min function pair by pair.

        reduce() repeatedly combines the current accumulated value with the
        next value in the list until one final result remains. An empty list
        returns 0 because there is no value to reduce.
        """
        if not isinstance(spells, list):
            raise ValueError(f"{C.RED}Object type is not a list.{C.RESET}")

        if not spells:
            return 0

        # Choose a two-argument function for reduce() based on operation name.
        if operation == "add":
            return reduce(operator.add, spells)
        elif operation == "multiply":
            return reduce(operator.mul, spells)
        elif operation == "max":
            return reduce(max, spells)
        elif operation == "min":
            return reduce(min, spells)
        else:
            raise ValueError(f"{C.RED}Unknown operation. Must be one of "
                             f"these values:{C.RESET}\n"
                             f"{C.RED}add / multiply / max / min{C.RESET}")

    @staticmethod
    def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
        """Return three specialized enchantment functions using partial().

        base_enchantment is a general function that expects power, element, and
        target. partial() creates new functions where power and element are
        already filled in.

        After partial(base_enchantment, 50, element), the returned function
        only needs the remaining target argument. Calling enchantment(target)
        is then equivalent to calling base_enchantment(50, element, target).
        """
        first_enchantment = partial(
            base_enchantment,
            50,
            random.choice(TestVariables.ENCHANTMENT_TYPES),
        )
        second_enchantment = partial(
            base_enchantment,
            50,
            random.choice(TestVariables.ENCHANTMENT_TYPES),
        )
        third_enchantment = partial(
            base_enchantment,
            50,
            random.choice(TestVariables.ENCHANTMENT_TYPES),
        )

        # The values in this dictionary are callable partial objects.
        return {"First_enchantment": first_enchantment,
                "Second_enchantment": second_enchantment,
                "Third_enchantment": third_enchantment}

    @staticmethod
    @lru_cache
    def memoized_fibonacci(n: int) -> int:
        """Return the nth Fibonacci number using recursion and lru_cache.

        Fibonacci is naturally recursive:
        F(0)=0, F(1)=1, and F(n)=F(n-1)+F(n-2).

        Without caching, the same smaller Fibonacci values are recalculated
        many times. lru_cache remembers previous results for the same n, so
        repeated recursive calls can reuse cached answers.

        The decorator order is important: lru_cache wraps the function first,
        then staticmethod keeps it callable from the class without self.
        """
        if n < 0:
            raise ValueError(
                f"{C.RED}Invalid input for n value. Must be >= 0.{C.RESET}")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            # Recursive case: use the same cached function for smaller values.
            return (
                AncientLibrary.memoized_fibonacci(n - 1) +
                AncientLibrary.memoized_fibonacci(n - 2)
                )

    @staticmethod
    def spell_dispatcher() -> Callable[[Any], str]:
        """Return a singledispatch function that routes by input type.

        singledispatch looks only at the type of the first argument. The
        default base_dispatcher handles unknown types. The registered functions
        handle int, str, and list inputs.

        The registered function names are `_` because they are not called
        directly. They are attached to base_dispatcher as type-specific
        handlers.
        """

        @singledispatch
        def base_dispatcher(spell_type: Any) -> str:
            return f"{C.RED}Unknown spell type!{C.RESET}"

        # Register specialized behavior for integer spell data.
        @base_dispatcher.register
        def _(spell_type: int) -> str:
            return "Damage spell"

        # Register specialized behavior for string spell data.
        @base_dispatcher.register
        def _(spell_type: str) -> str:
            return "Enchantment spell"

        # Register specialized behavior for list spell data.
        @base_dispatcher.register
        def _(spell_type: list) -> str:
            return "Multi-cast spell"

        # Return the configured dispatcher so callers can use it later.
        return base_dispatcher


class TesterFunctions:
    """Manual test helpers for each functools exercise requirement."""

    @staticmethod
    def reducer_tester() -> None:
        """Generate spell powers and test every supported reduce operation."""
        spell_power_list = TestVariables.POWER_VALUES

        print(f"{C.GREEN}Spell power values:{C.RESET} {spell_power_list}")
        print(f"{C.YELLOW}Sum:{C.RESET} "
              f"{AncientLibrary.spell_reducer(spell_power_list, 'add')}\n"
              f"{C.YELLOW}Multiply:{C.RESET} "
              f"{AncientLibrary.spell_reducer(spell_power_list, 'multiply')}\n"
              f"{C.YELLOW}Max Spell:{C.RESET} "
              f"{AncientLibrary.spell_reducer(spell_power_list, 'max')}\n"
              f"{C.YELLOW}Min Spell:{C.RESET} "
              f"{AncientLibrary.spell_reducer(spell_power_list, 'min')}\n")

    @staticmethod
    def partial_tester() -> None:
        """Create a base function, then test the partial enchantment functions.
        """

        # This general function is intentionally not partial yet.
        def base_enchantment(power: int, element: str, target: str) -> str:
            return (f"{element.capitalize()} enchantment with {power} power "
                    f"applied to {C.GREEN}{target}{C.RESET}")

        target = random.choice(TestVariables.ENCHANTMENT_ITEMS)
        enchantments = AncientLibrary.partial_enchanter(base_enchantment)

        print(f"{C.GREEN}Target item:{C.RESET} {target}\n")

        # Each enchantment is a partial function waiting only for target.
        for name, enchantment in enchantments.items():
            print(f"{C.YELLOW}{name}:{C.RESET} {enchantment(target)}")

    @staticmethod
    def fibonacci_tester() -> None:
        """Call memoized Fibonacci values and show cache statistics."""

        start = 0
        while start <= 20:
            print(f"Fib({start}): {AncientLibrary.memoized_fibonacci(start)}")
            start += 5

        # hits: How many times Python reused an already-calculated result from
        # the cache.

        # misses: How many times Python did not have the result yet, so it had
        # to actually calculate it.

        # maxsize: Maximum number of results the cache can store. With plain
        # @lru_cache, the default is usually 128.

        # currsize: How many results are currently stored in the cache.
        print(f"\n{C.YELLOW}Cache info:{C.RESET} "
              f"{AncientLibrary.memoized_fibonacci.cache_info()}")

    @staticmethod
    def dispatcher_tester() -> None:
        """Send different value types through the singledispatch dispatcher."""

        # spell_dispatcher returns the configured singledispatch function.
        dispatcher = AncientLibrary.spell_dispatcher()
        test_values = [
            random.choice(TestVariables.POWER_VALUES),
            random.choice(TestVariables.ENCHANTMENT_TYPES),
            TestVariables.ENCHANTMENT_ITEMS[:3],
            42.42,
        ]

        # The dispatcher chooses the registered handler from each value's type.
        for value in test_values:
            if isinstance(value, int):
                print(f"{C.YELLOW}Test value as int ({value}):{C.RESET} "
                      f"{dispatcher(value)}")
            elif isinstance(value, str):
                print(f"{C.YELLOW}Test value as str ({value}):{C.RESET} "
                      f"{dispatcher(value)}")
            elif isinstance(value, list):
                print(f"{C.YELLOW}Test value as list ({value}):{C.RESET} "
                      f"{dispatcher(value)}")
            else:
                print(f"{C.YELLOW}Test value as Any ({value}):{C.RESET} "
                      f"{dispatcher(value)}")


def main() -> None:
    print(f"{C.BLUE}***** Testing Ancient Libraries *****{C.RESET}")

    try:
        print(f"{C.PURPLE}\nTesting Spell Reducer...{C.RESET}")
        TesterFunctions.reducer_tester()

        print(f"{C.PURPLE}\nTesting Partial Enchanter...{C.RESET}")
        TesterFunctions.partial_tester()

        print(f"{C.PURPLE}\nTesting Memoized Fibonacci...{C.RESET}")
        TesterFunctions.fibonacci_tester()

        print(f"{C.PURPLE}\nTesting Spell Dispatcher...{C.RESET}")
        TesterFunctions.dispatcher_tester()
    except Exception as error:
        # Print both the exception type and message for easier debugging.
        print(f"{C.BG_RED}Exception Caught:{C.RESET} "
              f"{C.RED}{type(error).__name__}{C.RESET} {error}")


if __name__ == "__main__":
    main()
