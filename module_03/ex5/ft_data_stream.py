#!/usr/bin/env python3

"""
This module introduces generator-based streaming workflows:
- Producing events lazily with `yield` (constant memory)
- Consuming streams with a processor that gathers simple analytics
- Implementing classic generator examples (Fibonacci and prime numbers)
"""

from enum import Enum
import random
import time


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


class EventStream:
    """Static data pools used by the stream generator (players, levels,
    events)."""

    class Players:
        """Player nickname pool used for event generation."""

        @staticmethod
        def player_list() -> list[str]:
            players = [
                "ShadowFenrir",
                "IronWarden",
                "LunarStrider",
                "CrimsonHex",
                "OakheartRanger",
                "Frostveil",
                "RuneSeeker",
                "NightbladeX",
                "StormValkyr",
                "SilverGriffin",
                "VoidHarbinger",
                "AshenSpecter",
                "BlightReaver",
                "ObsidianFang",
                "CelestialRogue",
                "DreadHowler",
                "EmberShade",
                "GrimSentinel",
                "VortexSlayer",
                "MoonlitWraith",
                "Thornblade",
                "ArcaneNomad",
                "BloodTalon",
                "MysticDrifter",
                "IronPhantom",
                "FeralTempest",
                "CinderKnight",
                "Hexbound",
                "Shiverbane",
                "RiftWalker",
            ]
            return players

    class Levels:
        """Level pool used for event generation."""

        @staticmethod
        def level_list() -> list[int]:
            levels = [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
            ]
            return levels

    class Events:
        """Event text pool used for event generation."""

        @staticmethod
        def event_list() -> list[str]:
            events = [
                "killed a monster",
                "found treasure",
                "leveled up",
                "completed a quest",
                "crafted an item",
                "joined a guild",
                "defeated a boss",
                "explored a dungeon",
                "discovered a secret area",
                "won a duel",
                "lost a duel",
                "traded with a merchant",
                "unlocked an achievement",
                "rescued a villager",
                "tamed a wild beast",
                "solved an ancient puzzle",
                "survived an ambush",
                "entered a PvP arena",
                "upgraded equipment",
                "gathered rare resources",
                "accepted a bounty contract",
                "cleared a raid",
                "escaped a trap",
                "completed a daily mission",
                "activated a magical artifact",
                "defended a stronghold",
                "discovered hidden lore",
                "earned bonus experience",
                "failed a quest",
                "reached a new milestone",
            ]
            return events


def event_generator():
    """Yield a stream of (player, level, event) tuples with a small delay to
    simulate real-time events."""
    player_name_list: list[str] = EventStream.Players.player_list()
    level_list: list[int] = EventStream.Levels.level_list()
    event_name_list: list[str] = EventStream.Events.event_list()

    # Produce a fixed number of events for the demo run
    for event in range(1000):
        complete_action = (
            random.choice(player_name_list),
            random.choice(level_list),
            random.choice(event_name_list),
        )
        yield complete_action
        time.sleep(0.001)


def event_processor() -> None:
    """Consume the event stream and print live events plus a summary analytics
    section."""
    # Create the generator instance (the stream source)
    events_series = event_generator()
    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    event_number = 1
    # Consume the stream lazily and update counters as events arrive
    for event in events_series:
        player_name, level, event_name = event
        print(
            f"{C.YELLOW}Event {event_number}:{C.RESET} "
            f"Player {C.GREEN}{player_name}{C.RESET} "
            f"(level {level}) {event_name}"
        )
        event_number += 1
        total_events += 1
        if level > 10:
            high_level += 1
        if event_name == "found treasure":
            treasure_events += 1
        if event_name == "leveled up":
            level_up_events += 1

    print(
        f"{C.BLUE}=== Stream Analytics ==={C.RESET}\n"
        f"{C.YELLOW}Total Events Processed:{C.RESET} {total_events}\n"
        f"{C.YELLOW}High Level Players (10+):{C.RESET} {high_level}\n"
        f"{C.YELLOW}Treasure Events:{C.RESET} {treasure_events}\n"
        f"{C.YELLOW}Level-up Events:{C.RESET} {level_up_events}\n"
    )


def fibonacci_generator():
    """Yield an infinite Fibonacci sequence starting at 0."""
    first_number = 0
    second_number = 1
    # Infinite stream: state is preserved between yields
    while True:
        yield first_number
        next_number = second_number + first_number
        first_number = second_number
        second_number = next_number


def fibonacci_processor(n: int) -> None:
    """Print the first n Fibonacci numbers by consuming the Fibonacci
    generator."""
    sequence = fibonacci_generator()
    i = 0
    print(f"{C.YELLOW}Fibonacci Sequence (first {n}):{C.RESET}", end=" ")
    while i < n:
        fibo_num = next(sequence)
        print(fibo_num, end=", " if i < n - 1 else "\n")
        i += 1


def prime_number_generator():
    """Yield an infinite sequence of prime numbers starting at 2."""
    checked_number = 2
    # Infinite stream: test each number and yield only primes
    while True:
        is_it_prime = True
        if checked_number < 2:
            is_it_prime = False
        else:
            divisor = 2
            while divisor * divisor <= checked_number:
                if checked_number % divisor == 0:
                    is_it_prime = False
                    break
                divisor += 1
        if is_it_prime:
            yield checked_number
        checked_number += 1


def prime_number_processor(n: int) -> None:
    """Print the first n prime numbers by consuming the prime generator."""
    sequence = prime_number_generator()
    i = 0
    print(f"{C.YELLOW}Prime Numbers (first {n}):{C.RESET}", end=" ")
    while i < n:
        prime_number = next(sequence)
        print(prime_number, end=", " if i < n - 1 else "\n")
        i += 1


def main() -> None:
    """Entry point: run the event stream demo and the generator sequence
    demos."""
    # Measure CPU process time for the full demo run
    start = time.process_time()
    print(f"{C.BLUE}=== Game Data Stream Processor ==={C.RESET}\n")

    print("Processing 1000 game events...")
    time.sleep(3)
    # Run the streaming event processor (prints live events + analytics)
    event_processor()
    end = time.process_time()
    print(
        f"{C.YELLOW}Memor Usage:{C.RESET} Constant (streaming)\n"
        f"{C.YELLOW}Process Time:{C.RESET} {round((end - start), 4)} seconds"
    )

    # Classic generator demos
    fibonacci_processor(10)
    prime_number_processor(5)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{C.BG_RED}Error:{C.RESET} {type(e).__name__} {e}")
