#!/usr/bin/env python3

"""
This module simulates a small achievement tracking system for a game:
- Randomly selects a group of players
- Assigns each player a random set of achievements
- Performs set analytics (union, intersection, and differences)
"""


from enum import Enum
import random


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


class Achievements:
    """Factory for the available achievement names used in the tracker."""

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
            "True Completionist"
        ]
        return achievements


class Players:
    """Factory for the available player nicknames used in the tracker."""

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
            "SilverGriffin"
        ]
        return players


def main() -> None:
    """Run the achievement tracker demo and print analytics results."""
    print(f"{C.BLUE}=== Achievement Tracker System ==={C.RESET}\n")

    # Pick a small random group of players for this run
    game_players = random.sample(Players.player_list(), 3)
    # Store each player's achievements as a set for fast membership and set
    # operations
    player_achievements: dict[str, set[str]] = {}

    for player in game_players:
        # Assign a random set of achievements to the current player
        randomized_achievements = set(
            random.sample(Achievements.achievement_list(), 6)
            )
        player_achievements[player] = randomized_achievements
        print(
            f"{C.YELLOW}\nPlayer {player} achievements:{C.RESET} "
            f"{randomized_achievements}\n"
            )

    print(f"\n{C.BLUE}=== Achievement Analytics ==={C.RESET}\n")

    # Union: all achievements that appear for at least one player
    unique_union_set = set.union(*player_achievements.values())
    print(f"{C.YELLOW}All unique achievements:{C.RESET} {unique_union_set}\n"
          f"{C.YELLOW}Total unique achievements:{C.RESET} "
          f"{len(unique_union_set)}\n")

    # Intersection: achievements shared by every player in the group
    intsec_achiev = set.intersection(*player_achievements.values())
    if len(intsec_achiev) == 0:
        print(f"{C.YELLOW}\nCommon to all players:{C.RESET} "
              f"{C.RED}No common achievements found{C.RESET}")
    else:
        print(f"{C.YELLOW}Common to all players:{C.RESET} {intsec_achiev}")

    rare_set = set()
    for achievement in unique_union_set:
        player_count = 0
        for player in player_achievements:
            if achievement in player_achievements[player]:
                player_count += 1
        if player_count == 1:
            rare_set.add(achievement)

    if len(rare_set) == 0:
        print(
            f"{C.YELLOW}Rare achievements:{C.RESET} "
            f"{C.RED}No rare achievements found{C.RESET}"
            )
    else:
        print(
            f"{C.YELLOW}Rare achievements (1 player):{C.RESET} {rare_set}\n"
            f"{C.YELLOW}Total rare achievements:{C.RESET} {len(rare_set)}\n"
            )

    # Pairwise comparison examples (player 1 vs player 2)
    player_1_2_common = set.intersection(player_achievements[game_players[0]],
                                         player_achievements[game_players[1]])
    print(f"{C.YELLOW}{game_players[0]} vs {game_players[1]} common:{C.RESET}"
          f"{player_1_2_common}")

    player_1_unique = set.difference(
        player_achievements[game_players[0]],
        set.union(player_achievements[game_players[1]]),
        set.union(player_achievements[game_players[2]]))
    print(f"{C.YELLOW}{game_players[0]} unique:{C.RESET} {player_1_unique}")

    player_2_unique = set.difference(
        player_achievements[game_players[1]],
        set.union(player_achievements[game_players[0]]),
        set.union(player_achievements[game_players[2]]))
    print(f"{C.YELLOW}{game_players[1]} unique:{C.RESET} {player_2_unique}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"{C.BG_RED}Error:{C.RESET} {type(error).__name__} {error}")
