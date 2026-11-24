#!/usr/bin/env python3

"""
Validate space mission and crew data with Pydantic.

This exercise demonstrates nested Pydantic models. SpaceMission contains a
list of CrewMember objects, so Pydantic validates both the mission fields and
every crew member inside the crew list.

The exercise also uses @model_validator(mode="after") for mission rules that
depend on the whole object, such as checking for a captain or commander in
the crew.
"""

import json

from datetime import datetime
from enum import Enum
from typing import ClassVar
from pydantic import BaseModel, Field, ValidationError, model_validator


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


class Rank(Enum):
    """Allowed rank values for a crew member.

    Pydantic can receive rank strings from JSON, such as "commander", and
    convert them to the matching Rank enum member.
    """

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Validated data model for one crew member.

    This model validates individual crew member information before a member
    is accepted into a SpaceMission. If a crew member inside the mission crew
    list is invalid, the whole SpaceMission validation fails.
    """

    # Text fields use length constraints from the subject.
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank

    # ClassVar constants are helpers for Field(). They are not Pydantic
    # model fields. ge means "greater than or equal" and le means
    # "less than or equal".
    MIN_AGE: ClassVar[int] = 18
    MAX_AGE: ClassVar[int] = 80
    age: int = Field(ge=MIN_AGE, le=MAX_AGE)

    specialization: str = Field(min_length=3, max_length=30)

    # Experience is also checked as a numeric range.
    MIN_XP: ClassVar[int] = 0
    MAX_XP: ClassVar[int] = 50
    years_experience: int = Field(ge=MIN_XP, le=MAX_XP)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Validated data model for one space mission.

    This model includes simple field validation and nested validation. The
    crew field is a list of CrewMember objects, so Pydantic checks each crew
    member using the CrewMember model.
    """

    # Basic mission fields use string length and numeric range constraints.
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime

    # Duration is limited to 1-3650 days, which is a maximum of 10 years.
    MIN_DAYS: ClassVar[int] = 1
    MAX_DAYS: ClassVar[int] = 3650
    duration_days: int = Field(ge=MIN_DAYS, le=MAX_DAYS)

    # The crew list must contain 1-12 CrewMember objects. min_length and
    # max_length check the length of the list, not a numeric value.
    MIN_CREW: ClassVar[int] = 1
    MAX_CREW: ClassVar[int] = 12
    crew: list[CrewMember] = Field(min_length=MIN_CREW, max_length=MAX_CREW)

    mission_status: str = "planned"

    # Budget is stored in millions and must stay inside the subject limits.
    MIN_BUD: ClassVar[float] = 1.0
    MAX_BUD: ClassVar[float] = 10000.0
    budget_millions: float = Field(ge=MIN_BUD, le=MAX_BUD)

    @model_validator(mode="after")
    def validation_rules(self) -> "SpaceMission":
        """Check mission rules that depend on the complete mission.

        These checks run after normal field validation. At this point,
        self.crew already contains validated CrewMember objects, so their
        fields can be accessed as member.rank, member.years_experience, and
        member.is_active.
        """
        # Mission IDs must start with M according to the subject.
        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Mission ID must start with 'M'!"
                )

        # Collect all captains and commanders. The mission is valid if this
        # list has at least one member after checking the whole crew.
        leader_list = []
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                leader_list.append(member)
        if len(leader_list) == 0:
            raise ValueError(
                "Must have at least one Commander or Captain"
                )

        # Long missions need at least half of the crew to have 5 or more
        # years of experience.
        if self.duration_days > 365:
            xp_list = []
            for member in self.crew:
                if member.years_experience >= 5:
                    xp_list.append(member)
            if len(xp_list) < (len(self.crew) / 2):
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                    )

        # Every crew member must be active before launch approval.
        for member in self.crew:
            if not member.is_active:
                raise ValueError(
                    "All crew members must be active"
                    )

        # An "after" model validator must return the validated object.
        return self


def print_valid_mission(mission: SpaceMission) -> None:
    """Display one validated mission and its crew members.

    The model has already been validated before this function is called.
    This function only controls the output format.
    """

    print(f"{C.GREEN}Valid mission created:{C.RESET}\n"
          f"{C.YELLOW}Mission:{C.RESET} {mission.mission_name}\n"
          f"{C.YELLOW}ID:{C.RESET} {mission.mission_id}\n"
          f"{C.YELLOW}Destination:{C.RESET} {mission.destination}\n"
          f"{C.YELLOW}Duration:{C.RESET} {mission.duration_days} days\n"
          f"{C.YELLOW}Budget:{C.RESET} ${mission.budget_millions}M\n"
          f"{C.YELLOW}Crew size:{C.RESET} {len(mission.crew)}\n"
          f"{C.YELLOW}Crew members:{C.RESET}\n")

    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )


def valid_mission() -> None:
    """Load one valid mission from JSON and validate it.

    json.load() converts the JSON file into Python data. The file contains a
    list of mission dictionaries, so missions[0] is one mission.

    SpaceMission(**mission_data) unpacks the dictionary and lets Pydantic
    validate the mission and all nested crew members.
    """

    with open("space_missions.json", "r") as file:
        missions = json.load(file)

    mission_data = missions[0]
    mission = SpaceMission(**mission_data)
    print_valid_mission(mission)


def invalid_mission() -> None:
    """Load one invalid mission from JSON and try to validate it.

    This function does not catch ValidationError. The error moves up to
    main(), where it is displayed as the expected validation failure.
    """

    with open("invalid_space_missions.json", "r") as file:
        missions = json.load(file)

    mission_data = missions[0]
    mission = SpaceMission(**mission_data)
    print_valid_mission(mission)


def main() -> None:
    """Run the valid and invalid mission validation demonstrations."""

    print(f"{C.BLUE}\nSpace Mission Crew Validation{C.RESET}\n"
          f"{C.BLUE}========================================{C.RESET}\n")
    valid_mission()
    print(f"\n{C.BLUE}========================================{C.RESET}")

    print(f"{C.RED}\n\nTesting invalid mission{C.RESET}\n"
          f"{C.RED}========================================{C.RESET}\n"
          f"{C.RED}\nExpected validation error:{C.RESET}")

    try:
        invalid_mission()
    except ValidationError as error:
        print(f"{C.BG_RED}{error}{C.RESET}")

    print(f"\n{C.RED}========================================{C.RESET}")


if __name__ == "__main__":
    main()
