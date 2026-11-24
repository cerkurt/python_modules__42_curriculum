#!/usr/bin/env python3

"""
Practice decorators, decorator factories, functools.wraps, and static methods.

This exercise is about wrapping functions with reusable behavior. A decorator
is usually a function that receives another function and returns a replacement
function. The replacement function normally calls the original function, but it
can add behavior before or after that call.

Important terms for this module:

- Decorator:
  A decorator is a callable that takes a function and returns another callable.
  The syntax @decorator above a function is shorthand for:
      function_name = decorator(function_name)

- Wrapper:
  The wrapper is the inner function returned by a decorator. After decoration,
  calling the original function name actually calls the wrapper. The wrapper
  can print messages, measure time, validate arguments, retry after errors, and
  then call the original function when appropriate.

- Decorator factory:
  A decorator factory is a function that creates a decorator. It is needed when
  the decorator itself needs settings. For example, power_validator(10) first
  remembers the minimum power, then returns the real decorator.

- functools.wraps:
  wraps(func) copies useful metadata from the original function to the wrapper,
  such as __name__ and __doc__. Without wraps, a decorated function may look
  like it is named "wrapper" instead of its original name.

- *args and **kwargs:
  These make wrappers flexible. *args receives positional arguments as a tuple.
  **kwargs receives keyword arguments as a dictionary. Passing them back with
  func(*args, **kwargs) calls the original function with the same arguments.

- staticmethod:
  A static method is a function stored inside a class that does not receive
  self. It belongs logically to the class, but it does not need data from a
  specific object instance.

The goal is to understand what function is being decorated, what wrapper is
called later, and how decorators can separate extra behavior from the original
function's main responsibility.
"""

from collections.abc import Callable
from functools import wraps
import time


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


class SpellFunctions:
    """Decorators and decorator factories used by the spell examples.

    The methods are grouped in this class for organization. They do not use
    object state, so they are called from the class directly.
    """

    @staticmethod
    def spell_timer(func: Callable) -> Callable:
        """Return a decorator wrapper that measures execution time.

        func is the original function being decorated. The returned
        spell_wrapper becomes the new callable that runs when the decorated
        function name is called.

        The wrapper prints before the original function runs, measures start
        and end time with time.perf_counter(), prints the elapsed time and
        returns the original function's result.
        """

        # wraps keeps metadata such as the original function name.
        @wraps(func)
        def spell_wrapper(*args, **kwargs):
            # func.__name__ is preserved by wraps, so it prints the spell name.
            print(f"Casting {func.__name__}...")
            start_time = time.perf_counter()

            # Call the original function with the same arguments received here.
            result = func(*args, **kwargs)

            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f"Spell completed in {total_time:.3f} seconds")

            # Return the original result so decoration does not change output.
            return result

        return spell_wrapper

    @staticmethod
    def power_validator(min_power: int) -> Callable:
        """Return a decorator factory that validates spell power.

        min_power is remembered by the returned decorator through a closure.
        This function returns power_decorator, which receives the original
        function. power_decorator then returns power_wrapper, which runs at
        call time.

        The subject says standalone decorated functions receive power as their
        first argument, while MageGuild.cast_spell receives self, spell_name,
        and power. To support both cases, this wrapper reads power from the
        keyword argument named "power" when available, otherwise it uses the
        last positional argument.
        """

        # This inner function receives the original function being decorated.
        def power_decorator(func: Callable) -> Callable:
            @wraps(func)
            # This wrapper runs instead of the original function at call time.
            def power_wrapper(*args, **kwargs):
                power = kwargs.get("power")
                if power is None:
                    # For cast_spell(self, spell_name, power), power is last.
                    power = args[-1]

                # If validation passes, call the original function normally.
                if power >= min_power:
                    return func(*args, **kwargs)
                # If validation fails, do not call the original function.
                return f"{C.RED}Insufficient power for this spell{C.RESET}"

            return power_wrapper

        return power_decorator

    @staticmethod
    def retry_spell(max_attempts: int) -> Callable:
        """Return a decorator factory that retries a function after exceptions.

        max_attempts is remembered by the returned decorator. The wrapper tries
        to call the original function. If the original function raises an
        exception, the wrapper retries until one attempt succeeds or all
        attempts are used.

        If an attempt succeeds, the successful result is returned immediately.
        If every attempt fails, a final failure message is returned.
        """
        # This inner function receives the original function being decorated.
        def retry_decorator(func: Callable) -> Callable:
            @wraps(func)
            def retry_wrapper(*args, **kwargs):
                for attempt in range(1, max_attempts + 1):
                    try:
                        # A successful call exits the wrapper immediately.
                        return func(*args, **kwargs)
                    except Exception:
                        # Print retry messages only before the final attempt.
                        if attempt < max_attempts:
                            print(f"Spell failed, retrying... "
                                  f"(attempt {attempt} / {max_attempts})")

                # Reaching this line means every attempt raised an exception.
                return (
                    f"Spell casting failed after "
                    f"{C.RED}{max_attempts}{C.RESET} attempts")

            return retry_wrapper

        return retry_decorator


class MageGuild:
    """Represent a guild that demonstrates static and instance methods.

    validate_mage_name is a static method because it does not need self.
    cast_spell is an instance method because it belongs to a MageGuild object
    and receives self automatically when called from an instance.
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True when name is at least 3 chars and letters/spaces only.

        This method does not use self or any instance data. That is why it is a
        static method. It can be called as MageGuild.validate_mage_name(name).
        """
        # First rule: the name must not be too short.
        if len(name) < 3:
            return False
        # Second rule: every character must be a letter or a space.
        for char in name:
            if not char.isalpha() and char != " ":
                return False
        return True

    @SpellFunctions.power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Return a success message when the power_validator allows casting.

        The decorator checks power before this method body runs. If power is
        too low, the decorator returns the insufficient-power message.
        """
        return f"Successfully cast {spell_name} with {power} power"


class TesterFunctions:
    """Manual test helpers for each decorator exercise requirement.    """

    @staticmethod
    def spell_timer_tester() -> None:
        """Create a timed fireball function and print its returned result."""

        # @spell_timer means: fireball = SpellFunctions.spell_timer(fireball).
        @SpellFunctions.spell_timer
        def fireball() -> str:
            time.sleep(0.1)
            return "Fireball cast!"

        result = fireball()
        print(f"{C.YELLOW}Result:{C.RESET} {result}")

    @staticmethod
    def power_validator_tester() -> None:
        """Test power_validator on a standalone function where power is first.
        """

        # This is a decorator factory: first remember 10, then decorate
        # lightning.
        print(f"{C.YELLOW}(Attempt casting a spell with 15 and 5 power when "
              f"minimum 10 is required by the decorator){C.RESET}\n")

        @SpellFunctions.power_validator(10)
        def lightning(power: int) -> str:
            return f"Lightning cast with {power} power"

        print(f"{C.GREEN}Sufficient power result:{C.RESET} {lightning(15)}")
        print(f"{C.RED}Insufficient power result:{C.RESET} {lightning(5)}")

    @staticmethod
    def retry_spell_tester() -> None:
        """Test retry_spell with one always-failing and one successful spell.
        """
        # This function always raises, so the retry decorator will exhaust
        # attempts.
        @SpellFunctions.retry_spell(3)
        def spell_retries() -> str:
            raise RuntimeError("Unstable spell failed")

        # This function succeeds immediately, so no retry message is printed.
        @SpellFunctions.retry_spell(3)
        def spell_scream() -> str:
            return "Waaaaaaagh spelled !"

        print(spell_retries())
        print(spell_scream())

    @staticmethod
    def mage_guild_tester() -> None:
        """Test static name validation and decorated instance spell casting."""
        guild_tester = MageGuild()

        print(f"{C.YELLOW}Valid name 'Merlin':{C.RESET} "
              f"{MageGuild.validate_mage_name('Merlin')}")
        print(f"{C.YELLOW}Invalid name 'Al12-':{C.RESET} "
              f"{MageGuild.validate_mage_name('Al12-')}")

        print(guild_tester.cast_spell("Lightning", 15))
        print(guild_tester.cast_spell("Lightning", 5))


def main() -> None:
    print(f"{C.BLUE}***** Testing Master's Tower *****{C.RESET}")

    try:
        print(f"{C.PURPLE}\nTesting Spell Timer...{C.RESET}")
        TesterFunctions.spell_timer_tester()

        print(f"{C.PURPLE}\nTesting Power Validator...{C.RESET}")
        TesterFunctions.power_validator_tester()

        print(f"{C.PURPLE}\nTesting Retry Spell...{C.RESET}")
        TesterFunctions.retry_spell_tester()

        print(f"{C.PURPLE}\nTesting Mage Guild...{C.RESET}")
        TesterFunctions.mage_guild_tester()
    except Exception as error:
        # Print both the exception type and message for easier debugging.
        print(f"{C.BG_RED}Exception Caught:{C.RESET} "
              f"{C.RED}{type(error).__name__}{C.RESET} {error}")


if __name__ == "__main__":
    main()
