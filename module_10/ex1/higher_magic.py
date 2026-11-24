#!/usr/bin/env python3


"""
Practice higher-order functions by creating spell-building functions.

This exercise is about functions that work with other functions. A normal
function usually receives data and returns data. A higher-order function can
receive a function as an argument, return a new function, or both.

Important terms for this module:

- Callable:
  A Callable type hint means "a value that can be called like a function". In
  this file, spell functions are Callable objects because they can be called
  with target and power arguments.

- Passing a function:
  Passing BasicFunctions.spell means passing the function itself. Passing
  BasicFunctions.spell(target, power) means calling the function immediately
  and passing its returned string. Higher-order functions need the function
  itself, not the result string.

- Returning a function:
  The functions in HighOrderFunctions create inner functions and return them.
  The returned function can be stored in a variable and called later.

- Closure:
  The returned inner function remembers values from the outer function. For
  example, the combined spell remembers spell1 and spell2 even after
  spell_combiner has finished running.

- Wrapper / generated function:
  The inner function is a new function that controls how and when the original
  spell functions are called. It can combine spells, change the power value,
  validate a condition, or run a sequence of spells.

The goal is to understand the difference between a function object and a
function call, and to see how small functions can be composed into more complex
behavior.
"""


import random
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
    """Local test data used by the tester functions."""

    SPELL_NAMES = [
        "fireball", "heal", "shield", "lightning", "freeze", "earthquake",
        "tornado", "tsunami", "flash", "darkness", "meteor", "blizzard"
    ]

    POWER_VALUES = [24, 14, 24]

    TARGET_NAMES = ['Dragon', 'Goblin', 'Wizard', 'Knight']


class BasicFunctions:
    """Simple spell-like functions used as input for higher-order functions.

    These functions are normal callables. They receive a target and a power,
    and they return a string. The higher-order functions later use them as
    building blocks.
    """
    @staticmethod
    def spell(target: str, power: int) -> str:
        """Return a basic spell-casting message.

        This is a normal function, not a higher-order function. It is used
        later as a callable argument. Passing BasicFunctions.spell passes this
        function itself. Calling BasicFunctions.spell(target, power) returns
        the message string immediately.
        """
        spell_name = random.choice(TestVariables.SPELL_NAMES)

        return (
            f"{C.YELLOW}{spell_name.capitalize()}{C.RESET} "
            f"is casted on "
            f"{C.BLUE}{target}{C.RESET} with "
            f"{C.YELLOW}{power}{C.RESET} damage")

    @staticmethod
    def heal(target: str, power: int) -> str:
        """Return a healing message with the same callable shape as spell().

        It receives the same arguments as spell(), so both functions can be
        used interchangeably by higher-order functions such as spell_combiner
        and spell_sequence.
        """
        return (f"{C.GREEN}Heal{C.RESET} restores {C.BLUE}{target}{C.RESET} "
                f"for {C.YELLOW}{power}{C.RESET} HP")

    @staticmethod
    def power_validator(target: str, power: int) -> bool:
        """Return True when the power is high enough to cast a spell.

        This is a condition function. conditional_caster receives this callable
        and uses its boolean result to decide whether another spell function
        should be called.
        """
        if power >= 15:
            return True
        return False


class HighOrderFunctions:
    """Functions that receive callables and return newly generated callables.

    Each method here is a higher-order function. They do not mainly process
    strings directly. Instead, they create a new function that will process the
    target and power later.
    """

    @staticmethod
    def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
        """Return a new spell function that calls spell1 and spell2.

        spell1 and spell2 are parameter names for callable spell functions.
        They are not called immediately. The inner combined_spell function
        remembers them and calls both later when combined_spell(target, power)
        is used.

        Returning the inner function creates a closure: combined_spell keeps
        access to spell1 and spell2 after spell_combiner has finished.
        """

        def combined_spell(target: str, power: int) -> tuple[str, str]:
            # Call both original spell functions with the same target and power
            return spell1(target, power), spell2(target, power)

        return combined_spell

    @staticmethod
    def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
        """Return a new spell function that multiplies power before casting.

        base_spell is the original spell function. multiplier is remembered by
        the returned inner function. When the new function is called later, it
        calls base_spell with power * multiplier.

        This does not cast immediately. It creates a specialized spell function
        that can be stored and called later.
        """

        def amplified_power(target: str, power: int) -> str:
            # Modify the power argument, then call the original base spell.
            return base_spell(target, power * multiplier)

        return amplified_power

    @staticmethod
    def conditional_caster(condition: Callable, spell: Callable) -> Callable:
        """Return a new spell function that casts only if condition is True.

        Condition is a callable that returns a boolean. spell is the callable
        to run when the condition passes. Both callables receive the same
        target and power arguments.

        This separates the validation rule from the spell action. The returned
        function decides at call time whether the spell should happen.
        """

        def condition_validator(target: str, power: int) -> str:
            # First ask the condition function whether this spell is allowed.
            if condition(target, power):
                return spell(target, power)
            return f"{C.RED}Spell fizzled :({C.RESET}"

        return condition_validator

    @staticmethod
    def spell_sequence(spells: list[Callable]) -> Callable:
        """Return a new spell function that calls every spell in a list.

        The spells list must contain callables that can all be called with the
        same target and power arguments. The higher-order functions themselves,
        such as spell_combiner or power_amplifier, should not be placed here
        directly. Their returned spell functions should be placed here instead.
        """

        def spell_series(target: str, power: int) -> list[object]:
            # Store each result because the sequence returns all spell outputs.
            casted_spells = []
            for spell in spells:
                # Every item in spells must be callable with target and power.
                casted_spells.append(spell(target, power))
            return casted_spells

        return spell_series


class TesterFunctions:
    """Manual test helpers for each higher-order function.

    These functions are not the main subject logic. They make the behavior easy
    to inspect in the terminal during evaluation.
    """

    @staticmethod
    def basic_spell_tester() -> None:
        """Show the output of one normal base spell function."""
        target_name = random.choice(TestVariables.TARGET_NAMES)
        power_value = random.choice(TestVariables.POWER_VALUES)

        casted = BasicFunctions.spell(
            target_name, power_value
            )
        print(casted)

    @staticmethod
    def combined_spell_tester() -> None:
        """Create a combined spell and call the returned function."""
        combined_spell = HighOrderFunctions.spell_combiner(
            BasicFunctions.spell, BasicFunctions.heal
            )

        target_name = random.choice(TestVariables.TARGET_NAMES)
        power_value = random.choice(TestVariables.POWER_VALUES)

        spell_result, heal_result = combined_spell(
            target_name, power_value
            )
        print(f"{spell_result} and {heal_result}")

    @staticmethod
    def amplifier_tester() -> None:
        """Create an amplified spell and show the changed power effect."""
        amplified_result = HighOrderFunctions.power_amplifier(
            BasicFunctions.spell, 3)

        power_value = random.choice(TestVariables.POWER_VALUES)
        target_name = random.choice(TestVariables.TARGET_NAMES)

        print(
            f"Original Casted Power: "
            f"{C.YELLOW}{power_value}{C.RESET}\n"
            f"Spell Casted with Amplified Power: "
            f"{amplified_result(target_name, power_value)}")

    @staticmethod
    def conditional_spell_tester() -> None:
        """Create a conditional spell and call it with shared test data."""
        conditional_spell = HighOrderFunctions.conditional_caster(
            BasicFunctions.power_validator, BasicFunctions.spell
            )

        power_value = random.choice(TestVariables.POWER_VALUES)
        target_name = random.choice(TestVariables.TARGET_NAMES)

        print(conditional_spell(target_name, power_value))

    @staticmethod
    def spell_sequence_tester() -> None:
        """Create a sequence containing base and generated spell functions."""

        power_value = random.choice(TestVariables.POWER_VALUES)
        target_name = random.choice(TestVariables.TARGET_NAMES)

        # First create normal callable spell functions from higher-order tools.
        combined_spell = HighOrderFunctions.spell_combiner(
            BasicFunctions.spell,
            BasicFunctions.heal,
        )
        amplified_spell = HighOrderFunctions.power_amplifier(
            BasicFunctions.spell,
            3,
        )
        conditional_spell = HighOrderFunctions.conditional_caster(
            BasicFunctions.power_validator,
            BasicFunctions.spell,
        )
        # spell_sequence needs functions that already accept target and power.
        total_spells = [
            BasicFunctions.spell,
            BasicFunctions.heal,
            combined_spell,
            amplified_spell,
            conditional_spell,
        ]

        spell_sequence = HighOrderFunctions.spell_sequence(total_spells)

        sequence_result = spell_sequence(
            target_name, power_value
            )
        for spell in sequence_result:
            # combined_spell returns a tuple, so join it before printing.
            if isinstance(spell, tuple):
                print(" and ".join(spell))
            else:
                print(spell)


def main() -> None:
    print(f"{C.BLUE}\n***** Testing Spell Magic *****{C.RESET}\n")

    is_error = False

    try:
        print(f"{C.PURPLE}\n* Testing Base Spell *{C.RESET}\n"
              f"{C.PURPLE}======================{C.RESET}")
        TesterFunctions.basic_spell_tester()

        print(f"{C.PURPLE}\n\n* Testing Combined Spell *{C.RESET}\n"
              f"{C.PURPLE}=========================={C.RESET}")
        TesterFunctions.combined_spell_tester()

        print(f"{C.PURPLE}\n\n* Testing Power Amplifiying *{C.RESET}\n"
              f"{C.PURPLE}============================={C.RESET}")
        TesterFunctions.amplifier_tester()

        print(
            f"{C.PURPLE}\n\n* Testing Conditional Spell *{C.RESET}\n"
            f"{C.PURPLE}================================={C.RESET}")
        TesterFunctions.conditional_spell_tester()

        print(
            f"{C.PURPLE}\n\n* Testing Spell Sequence *{C.RESET}\n"
            f"{C.PURPLE}=================================={C.RESET}"
            )
        TesterFunctions.spell_sequence_tester()
    except Exception as error:
        # Print both the exception type and message for easier debugging.
        print(f"{C.BG_RED}Exception Caught:{C.RESET} "
              f"{C.RED}{type(error).__name__}{C.RESET} {error}")
        is_error = True

    if not is_error:
        print(f"\n\n{C.GREEN}All spell tests are successful!{C.RESET}")


if __name__ == "__main__":
    main()
