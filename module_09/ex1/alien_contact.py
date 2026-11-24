#!/usr/bin/env python3

"""
Validate alien contact reports with Pydantic.

This exercise adds two new ideas on top of basic field validation:
- Enum is used when a field must be one of a fixed set of values;
- @model_validator(mode="after") is used for rules that depend on
  more than one field.

The JSON files contain raw dictionaries. AlienContact validates those
dictionaries and turns valid ones into Python objects.
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


class ContactType(Enum):
    """Allowed contact types for an alien contact report.

    Enum is useful here because the subject gives a fixed list of accepted
    values. Pydantic can receive strings such as "radio" from JSON and
    convert them to the matching enum member.
    """

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Validated data model for one alien contact report.

    Field() handles simple checks such as string length and number ranges.
    The model_validator below handles business rules that need to compare
    multiple fields, such as contact type and witness count.
    """

    # Basic field constraints: length checks for strings and range checks
    # for numbers. These are checked before the model_validator runs.
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)

    # The enum limits this field to radio, visual, physical, or telepathic.
    contact_type: ContactType

    # ClassVar constants are helpers for Field(). They are not model fields.
    # ge means "greater than or equal" and le means "less than or equal".
    MIN_SIG: ClassVar[float] = 0.0
    MAX_SIG: ClassVar[float] = 10.0
    signal_strength: float = Field(ge=MIN_SIG, le=MAX_SIG)

    MIN_DUR: ClassVar[int] = 1
    MAX_DUR: ClassVar[int] = 1440
    duration_minutes: int = Field(ge=MIN_DUR, le=MAX_DUR)

    MIN_WIT: ClassVar[int] = 1
    MAX_WIT: ClassVar[int] = 100
    witness_count: int = Field(ge=MIN_WIT, le=MAX_WIT)

    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validation_rules(self) -> "AlienContact":
        """Check business rules that depend on multiple fields.

        This validator runs after Pydantic has already checked the simple
        field rules. Raising ValueError here makes Pydantic wrap the problem
        inside a ValidationError.
        """
        # startswith() checks the required prefix for the contact ID.
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC'"
                )

        # Physical contact is only accepted when the report is verified.
        if (self.contact_type is ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError(
                "Physical conctact reports must be verified!"
                )

        # Telepathic contact needs several witnesses because it is harder
        # to verify than a normal visual or radio report.
        if (self.contact_type is ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contract requires at least 3 witnesses"
                )

        # A strong signal should include a message. None and an empty string
        # both mean that no useful message was provided.
        if self.signal_strength > 7.0 and (
                self.message_received is None or self.message_received == ""):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
                )

        # An "after" model validator must return the validated object.
        return self


def print_valid_contact(contact: AlienContact) -> None:
    """Display one validated contact report in a readable format.

    Validation and printing are kept separate. This function expects an
    already validated AlienContact object and only handles terminal output.
    """

    print(f"{C.GREEN}Valid contact report:{C.RESET}\n"
          f"{C.YELLOW}ID:{C.RESET} {contact.contact_id}\n"
          f"{C.YELLOW}Type:{C.RESET} {contact.contact_type.value}\n"
          f"{C.YELLOW}Location:{C.RESET} {contact.location}\n"
          f"{C.YELLOW}Signal:{C.RESET} {contact.signal_strength}/10\n"
          f"{C.YELLOW}Duration:{C.RESET} {contact.duration_minutes} minutes\n"
          f"{C.YELLOW}Witnesses:{C.RESET} {contact.witness_count}\n"
          f"{C.YELLOW}Time:{C.RESET} "
          f"{contact.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
          f"{C.YELLOW}Message:{C.RESET} '{contact.message_received}'"
          )


def valid_contact() -> None:
    """Load one valid contact from JSON and validate it.

    json.load() converts the JSON text into Python data. The file contains a
    list of dictionaries, so contacts[0] is one contact report dictionary.

    AlienContact(**contact_data) unpacks that dictionary into keyword
    arguments and starts Pydantic validation.
    """

    with open("alien_contacts.json", "r") as file:
        contacts = json.load(file)

    contact_data = contacts[0]
    contact = AlienContact(**contact_data)
    print_valid_contact(contact)


def invalid_contact() -> None:
    """Load one invalid contact from JSON and try to validate it.

    This function does not catch ValidationError. The error is allowed to
    move up to main(), where it is displayed as the expected invalid case.
    """

    with open("invalid_contacts.json", "r") as file:
        contacts = json.load(file)

    contact_data = contacts[0]
    contact = AlienContact(**contact_data)
    print_valid_contact(contact)


def main() -> None:
    """Run the valid and invalid contact validation demonstrations."""

    print(f"{C.BLUE}\nAlien Contact Log Validation{C.RESET}\n"
          f"{C.BLUE}========================================{C.RESET}\n")
    valid_contact()
    print(f"\n{C.BLUE}========================================{C.RESET}")

    print(f"{C.RED}\n\nTesting invalid contact{C.RESET}\n"
          f"{C.RED}========================================{C.RESET}\n"
          f"{C.RED}\nExpected validation error:{C.RESET}")

    try:
        invalid_contact()
    except ValidationError as error:
        print(f"{C.BG_RED}{error}{C.RESET}")

    print(f"\n{C.RED}========================================{C.RESET}")


if __name__ == "__main__":
    main()
