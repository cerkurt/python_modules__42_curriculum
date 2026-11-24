#!/usr/bin/env python3


# python3 -m venv .venv
# source .venv/bin/activate
# python3 -m pip install pydantic mypy
"""
Validate space station data with Pydantic.

This exercise demonstrates the basic Pydantic workflow:
- define a model with typed fields;
- add field constraints with Field();
- create model instances from raw data;
- let Pydantic raise ValidationError when the data is invalid.

The JSON files contain raw dictionaries. The SpaceStation model turns those
dictionaries into validated Python objects.
"""

import json

from datetime import datetime
from typing import ClassVar
from pydantic import BaseModel, Field, ValidationError


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


class SpaceStation(BaseModel):
    """Validated data model for one space station.

    BaseModel makes this class a Pydantic model. When a SpaceStation object
    is created, Pydantic checks the type annotations and the Field()
    constraints below. If any value is invalid, object creation fails with
    a ValidationError.
    """

    # String fields use min_length and max_length to limit text size.
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)

    # ClassVar marks these constants as helper values, not model fields.
    # ge means "greater than or equal" and le means "less than or equal".
    MIN_CREW: ClassVar[int] = 1
    MAX_CREW: ClassVar[int] = 20
    crew_size: int = Field(ge=MIN_CREW, le=MAX_CREW)

    # Power and oxygen are percentages, they must stay between 0 and 100.
    MIN_POWER: ClassVar[float] = 0.0
    MAX_POWER: ClassVar[float] = 100.0
    power_level: float = Field(ge=MIN_POWER, le=MAX_POWER)

    MIN_OXY: ClassVar[float] = 0.0
    MAX_OXY: ClassVar[float] = 100.0
    oxygen_level: float = Field(ge=MIN_OXY, le=MAX_OXY)

    # Pydantic can convert a valid datetime string from JSON into datetime.
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def print_valid_station(station: SpaceStation) -> None:
    """Display one validated station in a readable format.

    The model is already validated before this function is called. This
    function only handles output formatting. Keeping printing separate from
    validation makes the model easier to reuse.
    """

    print(f"{C.GREEN}Valid station created:{C.RESET}\n"
          f"{C.YELLOW}ID:{C.RESET} {station.station_id}\n"
          f"{C.YELLOW}Name:{C.RESET} {station.name}\n"
          f"{C.YELLOW}Crew:{C.RESET} {station.crew_size} people\n"
          f"{C.YELLOW}Power:{C.RESET} {station.power_level}%\n"
          f"{C.YELLOW}Oxygen:{C.RESET} {station.oxygen_level}%\n"
          f"{C.YELLOW}Last maintenance:{C.RESET} "
          f"{station.last_maintenance.strftime('%Y-%m-%d %H:%M:%S')}\n"
          f"{C.YELLOW}Status:{C.RESET} "
          f"{'Operational' if station.is_operational else 'Offline'}\n"
          f"{C.YELLOW}Notes:{C.RESET} {station.notes}"
          )


def valid_station() -> None:
    """Load one valid station from JSON and validate it.

    json.load() converts the JSON file into normal Python data. In this case,
    the file contains a list of dictionaries, so stations[0] is one station
    dictionary.

    SpaceStation(**station_data) unpacks the dictionary and passes its keys as
    keyword arguments to the Pydantic model. This is the point where Pydantic
    validates the raw data.
    """

    with open("space_stations.json", "r") as file:
        stations = json.load(file)

    station_data = stations[0]
    station = SpaceStation(**station_data)
    print_valid_station(station)


def invalid_station() -> None:
    """Load one invalid station from JSON and try to validate it.

    This function does not catch the ValidationError itself. The error is
    allowed to move up to main(), where it is caught and displayed.
    """

    with open("invalid_stations.json", "r") as file:
        stations = json.load(file)

    station_data = stations[0]
    station = SpaceStation(**station_data)
    print_valid_station(station)


def main() -> None:
    """Run the valid and invalid validation demonstrations."""

    print(f"{C.BLUE}\nSpace Station Data Validation{C.RESET}\n"
          f"{C.BLUE}========================================{C.RESET}\n")
    valid_station()
    print(f"\n{C.BLUE}========================================{C.RESET}")

    print(f"{C.RED}\n\nTesting invalid station{C.RESET}\n"
          f"{C.RED}========================================{C.RESET}\n"
          f"{C.RED}\nExpected validation error:{C.RESET}")
    try:
        invalid_station()
    except ValidationError as error:
        print(f"{C.BG_RED}{error}{C.RESET}")

    print(f"\n{C.RED}========================================{C.RESET}")


if __name__ == "__main__":
    main()
