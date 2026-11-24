#!/usr/bin/env python3

"""
Practice closures, nonlocal variables, and functions that remember state.

This exercise is about scope: where variables live, how long they live, and
which functions can access them. The main pattern is an outer function that
creates a variable, defines an inner function, and returns that inner function.

Important terms for this module:

- Scope:
  Scope means the area of code where a variable can be used. A variable created
  inside a function normally belongs only to that function.

- Closure:
  A closure happens when an inner function uses a variable from an outer
  function, and the outer function returns the inner function. Even after the
  outer function has finished, Python keeps the needed outer variable alive.

  General shape:
      def outer():
          remembered_value = something

          def inner():
              use remembered_value

          return inner

- Persistent private state:
  The remembered variable behaves like private state. Code outside the closure
  cannot directly access it, but the returned inner function can keep using it.
  This lets us remember values without using global variables or classes.

- nonlocal:
  nonlocal is needed when an inner function wants to reassign a variable from
  the nearest outer function scope. For example, count += 1 is a reassignment,
  so Python must be told that count belongs to the outer function.

- Mutating vs reassigning:
  Changing the contents of a dictionary, such as memory[key] = value, mutates
  the dictionary object. It does not reassign the variable memory, so nonlocal
  is not needed in that case. But assigning memory = {} inside the inner
  function would require nonlocal.

The goal is to understand where the remembered data lives and why each returned
function can keep using it later.
"""

# nonlocal: only when the inner function needs to change a variable from the
# outer function. Without nonlocal, Python assumes count is a new local
# variable inside the inner function, and then it gets confused because you are
# reading it before assigning it.


from collections.abc import Callable


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
    """Local test data for the enchantment factory demonstrations."""

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


class MysteryFunctions:
    """Functions that create closures and demonstrate remembered state.

    Each method returns either an inner function or a dictionary containing
    inner functions. The important part is that the inner functions keep access
    to variables created in the outer function.
    """

    @staticmethod
    def mage_counter() -> Callable:
        """Return a counter function that remembers its own call count.

        call_count belongs to mage_counter(), but inner_counter() uses it. When
        mage_counter() returns inner_counter, Python keeps call_count alive.

        nonlocal is required because inner_counter reassigns call_count with
        call_count += 1. Without nonlocal, Python would treat call_count as a
        new local variable inside inner_counter and raise an UnboundLocalError.

        Each call to mage_counter() creates a separate closure with its own
        independent call_count value.
        """
        call_count = 0

        def inner_counter() -> int:
            """Increase and return the remembered call count."""
            nonlocal call_count
            call_count += 1
            return call_count

        return inner_counter

    @staticmethod
    def spell_accumulator(initial_power: int) -> Callable:
        """Return a function that remembers and updates total spell power.

        start_value begins as initial_power. The returned power_accumulator()
        function remembers that value between calls.

        nonlocal is needed because start_value is reassigned with +=. Every
        call adds the new accumulation_value to the same remembered total and
        returns the updated total.
        """
        start_value = initial_power

        def power_accumulator(accumulation_value: int) -> int:
            """Add to the remembered total and return the new value."""
            nonlocal start_value
            start_value += accumulation_value
            return start_value

        return power_accumulator

    @staticmethod
    def enchantment_factory(enchantment_type: str) -> Callable:
        """Return a function that remembers one enchantment type.

        This is a read-only closure. item_describer() uses enchantment_type
        from the outer function, but it does not modify it. Because there is no
        reassignment, nonlocal is not needed.

        Calling enchantment_factory("Flaming") returns a function that can
        later receive an item name and produce strings like "Flaming Sword".
        """

        def item_describer(item_name: str) -> str:
            """Combine the remembered enchantment type with a new item name."""
            return f"{enchantment_type} {item_name}"

        return item_describer

    @staticmethod
    def memory_vault() -> dict[str, Callable]:
        """Return store and recall functions that share one private dictionary.

        memory is created inside memory_vault(), so outside code cannot access
        it directly. The returned store() and recall() functions both close
        over the same dictionary.

        store() mutates the dictionary with memory[key] = value. This does not
        require nonlocal because the variable memory itself is not reassigned.

        recall() reads from the same remembered dictionary. It checks key
        existence before indexing, because memory[key] would raise KeyError if
        the key is missing.
        """
        memory = {}

        def store(key: str, value: object) -> None:
            """Save one value under one key in the remembered dictionary."""
            memory[key] = value

        def recall(key: str) -> object:
            """Return the stored value for key, or a readable missing message.
            """
            if key not in memory:
                return f"{C.RED}Memory not found :({C.RESET}"
            return memory[key]

        return {"store": store, "recall": recall}


class TesterFunctions:
    """Manual test helpers for each closure exercise requirement.

    These functions are not the main subject logic. They show how the returned
    inner functions keep their remembered state across multiple calls.
    """

    @staticmethod
    def counter_tester() -> None:
        """Show that two counters have separate remembered call counts."""
        # Each mage_counter() call creates a new independent closure.
        counter_a = MysteryFunctions.mage_counter()
        counter_b = MysteryFunctions.mage_counter()

        iterator = 1
        while iterator <= 10:
            print(f"{C.YELLOW}Function call {iterator} for "
                  f"counter_a:{C.RESET} {counter_a()}")

            # counter_b proves that a second closure keeps a separate count.
            if iterator == 4 or iterator == 6 or iterator == 9:
                print(f"{C.GREEN}\nFunction call for counter_b: "
                      f"{C.RESET}{C.GREEN}{counter_b()}{C.RESET}\n")

            iterator += 1

    @staticmethod
    def accumulator_tester() -> None:
        """Show that the accumulator remembers its updated total."""
        # accumulated_result is the returned inner function, not a number.
        base_power = 100
        accumulated_result = MysteryFunctions.spell_accumulator(base_power)

        accumulator = 20
        while accumulator <= base_power:
            print(f"Base power: {C.YELLOW}{base_power}{C.RESET}, add "
                  f"{C.YELLOW}{accumulator}{C.RESET}: "
                  f"{C.YELLOW}{accumulated_result(accumulator)}{C.RESET}")
            accumulator += 10

    @staticmethod
    def factory_tester() -> None:
        """Create enchantment functions and apply them to generated items."""

        for enchantment_type in TestVariables.ENCHANTMENT_TYPES[:3]:
            # The returned function remembers this loop's enchantment_type.
            factory_item = MysteryFunctions.enchantment_factory(
                enchantment_type)

            for enchantment_item in (
                    TestVariables.ENCHANTMENT_ITEMS[:2]):
                print(
                    f"{C.YELLOW}Enchantment Type:{C.RESET} "
                    f"{enchantment_type}\n"
                    f"{C.YELLOW}Enchantment Item:{C.RESET} "
                    f"{enchantment_item}\n"
                    f"{C.YELLOW}Factory Item:{C.RESET} "
                    f"{factory_item(enchantment_item)}\n"
                    )

    @staticmethod
    def memory_tester() -> None:
        """Store and recall values through the functions returned by the
        vault."""

        # secret_info is a dictionary of functions, not the memory dictionary.
        secret_info = MysteryFunctions.memory_vault()
        secret_info["store"]("secret", 42)

        print(f"{C.YELLOW}Storing the 'secret' info:{C.RESET} 42")
        print(
            f"{C.YELLOW}Recalling the 'secret':{C.RESET} "
            f"{secret_info['recall']('secret')}\n"
            f"{C.YELLOW}Recalling 'test_value':{C.RESET} "
            f"{secret_info['recall']('test_value')}"
        )


def main() -> None:
    print(f"{C.BLUE}***** Testing Scope Mysteries *****{C.RESET}")

    try:
        print(f"{C.PURPLE}\nTesting Mage Counter...{C.RESET}")
        TesterFunctions.counter_tester()

        print(f"{C.PURPLE}\nTesting Spell Power Accumulator...{C.RESET}")
        TesterFunctions.accumulator_tester()

        print(f"{C.PURPLE}\nTesting Enchantment Factory...{C.RESET}")
        TesterFunctions.factory_tester()

        print(f"{C.PURPLE}\nTesting Memory Vault...{C.RESET}")
        TesterFunctions.memory_tester()
    except Exception as error:
        # Print both the exception type and message for easier debugging.
        print(f"{C.BG_RED}Exception Caught:{C.RESET} "
              f"{C.RED}{type(error).__name__}{C.RESET} {error}")


if __name__ == "__main__":
    main()
