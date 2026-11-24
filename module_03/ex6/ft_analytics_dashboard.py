#!/usr/bin/env python3

"""
This module combines list, dictionary, and set operations to simulate
a small analytics dashboard for a game system.

It demonstrates:
- Nested dictionaries to represent player profiles
- List-based filtering logic
- Dictionary aggregation and categorization
- Set operations (union, intersection, difference)
- Combined statistical reporting
"""

from enum import Enum
import random

# IMPORTANT: THIS EXERCISE DID NOT USE LIST AND DICT COMPREHENSIONS.
# IT NEEDS TO BE EDITED. MODULE DID NOT PASS WITH THE FULL SCORE.


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
    """Static data pools used for generating randomized dashboard data."""

    class Players:
        """Available player nickname pool."""

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
            ]
            return players

    class Achievements:
        """Available achievement pool."""

        @staticmethod
        def achievement_list() -> list[str]:
            achievements = [
                "Graveyard Shift",
                "Silver Tongue",
                "Relic Hunter",
                "Unbreakable",
                "Monster Contract Veteran",
                "Herbalist`s Apprentice",
                "Path of Blades",
                "Treasure Beneath the Ruins",
                "Beast Whisperer",
                "Coin Collector",
                "Wanderer of the Wilds",
                "Master of Preparation",
                "Trial by Fire",
                "Lone Survivor",
                "Arcane Scholar",
                "Shadow Walker",
                "Legend in the Making",
                "No Mercy",
                "Ancient Secrets",
                "True Completionist",
            ]
            return achievements

    class Scores:
        """Available score value pool."""

        @staticmethod
        def score_list() -> list[int]:
            scores = [
                500,
                600,
                700,
                800,
                900,
                1000,
                1100,
                1200,
                1300,
                1400,
                1500,
                1600,
                1700,
                1800,
                1900,
                2000,
                2100,
                2200,
                2300,
                2400,
                2500,
                2600,
                2700,
                2800,
                2900,
                3000,
                3100,
                3200,
                3300,
                3400,
                3500,
                3600,
                3700,
                3800,
                3900,
                4000,
                4100,
                4200,
                4300,
                4400,
                4500,
                4600,
                4700,
                4800,
                4900,
                5000,
            ]
            return scores

    class Regions:
        """Available region pool."""

        @staticmethod
        def region_list() -> list[str]:
            regions = [
                "North",
                "East",
                "West",
                "South",
                "Central",
                "Mountains",
                "Coast",
                "Highlands",
                "Valley",
                "Marsh",
                "Desert",
                "Isles",
                "Forest",
                "Plateau",
                "Tundra",
            ]
            return regions


def player_profile_info() -> dict[str, dict[str, int | list[str]]]:
    """Generate a randomized player profile dictionary with scores and
    achievements."""
    player_profile = {}
    # Randomly select players and assign random scores
    player_names = random.sample(EventStream.Players.player_list(), 10)
    player_scores = random.sample(EventStream.Scores.score_list(), 10)

    for name, score in zip(player_names, player_scores):
        player_detail = {}
        achievement_count = random.randint(1, 6)
        player_detail["score"] = score
        # Assign a random subset of achievements per player
        player_detail["achievements"] = random.sample(
            EventStream.Achievements.achievement_list(), achievement_count
        )
        player_profile[name] = player_detail

    return player_profile


# def name_score_pair() -> dict[str, int]:
#     player_names = random.sample(EventStream.Players.player_list(), 6)
#     player_scores = random.sample(EventStream.Scores.score_list(), 6)

#     score_profile = {}
#     for name, score in zip(player_names, player_scores):
#         score_profile[name] = score

#     print(score_profile)
#     return score_profile


def list_comp_exmp(
    player_profile: dict[str, dict[str, int | list[str]]],
) -> None:
    """Demonstrate list-based filtering logic on the player profile."""
    high_score_list = []
    # Players with score greater than 2000
    for key, value in player_profile.items():
        if value["score"] > 2000:
            high_score_list.append(key)

    double_score_list = []
    # Scores divisible by 600
    for key, value in player_profile.items():
        if value["score"] % 600 == 0:
            double_score_list.append(value["score"])

    active_player_list = []
    # Players considered highly active
    for key, value in player_profile.items():
        if value["score"] > 3500:
            active_player_list.append(key)

    print(
        f"{C.YELLOW}High Scores (>2000):{C.RESET} {high_score_list}\n"
        f"{C.YELLOW}Scores Doubled:{C.RESET} {double_score_list}\n"
        f"{C.YELLOW}Active Players:{C.RESET} {active_player_list}"
    )


def dict_comp_exmp(
    player_profile: dict[str, dict[str, int | list[str]]],
) -> None:
    """Demonstrate dictionary aggregation and categorization logic."""
    name_score_pair = {}
    # Project nested profile into name -> score view
    for name, profile in player_profile.items():
        name_score_pair[name] = profile["score"]

    # Categorize players based on score thresholds
    score_category = {}
    score_category["high_score"] = []
    score_category["medium_score"] = []
    score_category["low_score"] = []

    for key, value in player_profile.items():
        if value["score"] >= 3500:
            score_category["high_score"].append(value)
        elif value["score"] < 3500 and value["score"] > 2000:
            score_category["medium_score"].append(value)
        else:
            score_category["low_score"].append(value)

    final_score_dict = {}
    final_score_dict["high"] = len(score_category["high_score"])
    final_score_dict["medium"] = len(score_category["medium_score"])
    final_score_dict["low"] = len(score_category["low_score"])

    achievement_count = {}
    # Count achievements per player
    for name, profile in player_profile.items():
        achievement_count[name] = len(profile["achievements"])

    print(
        f"{C.YELLOW}Player Scores:{C.RESET} {name_score_pair}\n"
        f"{C.YELLOW}Score Categories:{C.RESET} {final_score_dict}\n"
        f"{C.YELLOW}Achievement Counts:{C.RESET} {achievement_count}"
    )


def set_comp_exmp() -> set:
    """Demonstrate set operations including union, intersection, and difference."""
    # Random player comparison sets
    random_player_set_1 = set(
        random.sample(EventStream.Players.player_list(), 6)
    )
    random_player_set_2 = set(
        random.sample(EventStream.Players.player_list(), 6)
    )
    player_intersection_set = random_player_set_1.intersection(
        random_player_set_2
    )
    player_union_set = random_player_set_1.union(random_player_set_2)

    # Random achievement comparison sets
    random_achievement_set_1 = set(
        random.sample(EventStream.Achievements.achievement_list(), 6)
    )

    random_achievement_set_2 = set(
        random.sample(EventStream.Achievements.achievement_list(), 6)
    )

    achievement_intersection_set = random_achievement_set_1.intersection(
        random_achievement_set_2
    )

    achievement_union_set = random_achievement_set_1.union(
        random_achievement_set_2
    )

    # Achievements appearing in only one set
    unique_achievements_set = (
        achievement_union_set - achievement_intersection_set
    )

    # Randomly selected active regions
    random_active_regions = set(
        random.sample(EventStream.Regions.region_list(), 5)
    )

    print(
        f"{C.YELLOW}Unique Players:{C.RESET} "
        f"{player_union_set - player_intersection_set}\n"
        f"{C.YELLOW}Unique Achievements:{C.RESET} "
        f"{unique_achievements_set}\n"
        f"{C.YELLOW}Active Regions:{C.RESET} {random_active_regions}"
    )
    return unique_achievements_set


def general_report(
    player_profile: dict[str, dict[str, int | list[str]]],
) -> tuple[int, int, float, tuple[str, int, int]]:
    """Compute overall statistics such as totals, averages, and top
    performer."""
    total_players = len(player_profile.keys())

    achievement_amount_dict = {}
    # Count how many players own each achievement
    for name, profile in player_profile.items():
        for achievement in profile["achievements"]:
            if achievement in achievement_amount_dict:
                achievement_amount_dict[achievement] += 1
            else:
                achievement_amount_dict[achievement] = 1

    unique_achievements_list = []
    # Achievements owned by exactly one player
    for achievement, count in achievement_amount_dict.items():
        if count == 1:
            unique_achievements_list.append(achievement)

    unique_achievements = len(unique_achievements_list)

    # Compute total score for average calculation
    total_score = 0
    for key, value in player_profile.items():
        total_score = total_score + value["score"]
    average_score = total_score / total_players

    # Determine highest scoring player
    top_name = None
    top_score = 0
    achievement_count = 0
    for name, profile in player_profile.items():
        if profile["score"] > top_score:
            top_score = profile["score"]
            top_name = name
            achievement_count = len(profile["achievements"])

    top_performer = (top_name, top_score, achievement_count)

    return (total_players, unique_achievements, average_score, top_performer)


def combined_analysis() -> None:
    """Print the formatted combined analytics summary from general_report."""
    final_tuple = general_report(full_player_profile)
    total_players, unique_achievements, average_score, top_performer = (
        final_tuple
    )
    name, score, achievement_count = top_performer

    print(
        f"{C.YELLOW}Total Players:{C.RESET} {total_players}\n"
        f"{C.YELLOW}Total Unique Achievements:{C.RESET} "
        f"{C.YELLOW}Average Score:{C.RESET} {average_score}\n"
        f"{C.YELLOW}Top Performer:{C.RESET} {name} ({score} points, "
        f"{achievement_count} achievements)"
    )


if __name__ == "__main__":
    full_player_profile = player_profile_info()
    print(f"{C.BLUE}=== Game Analytics Dashboard ==={C.RESET}")
    try:
        print(f"{C.YELLOW}\n=== List Comprehension Examples ==={C.RESET}")
        list_comp_exmp(full_player_profile)

        print(f"{C.YELLOW}\n=== Dict Comprehension Examples ==={C.RESET}")
        dict_comp_exmp(full_player_profile)

        print(f"{C.YELLOW}\n=== Set Comprehension Examples ==={C.RESET}")
        set_comp_exmp()

        print(f"{C.YELLOW}\n=== Combined Analysis ==={C.RESET}")
        combined_analysis()

    except Exception as e:
        print(f"{C.BG_RED}Error:{C.RESET} {type(e).__name__} {e}")
