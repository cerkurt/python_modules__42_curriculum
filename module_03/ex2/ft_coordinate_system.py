#!/usr/bin/env python3

"""
This module demonstrates the use of:
- Tuples to represent immutable 3D coordinates (x, y, z)
- Command-line argument parsing with sys.argv
- Euclidean distance calculation using math.sqrt
- Graceful error handling with try/except blocks

The program parses a 3D position from command-line arguments, prints a creation
summary, and showcases both a valid and an invalid parsing demonstration.
"""

from enum import Enum
import sys
import math


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


def coordtinate_tuple_unpack(coord: tuple[int, int, int]) -> str:
    """Format a 3D coordinate tuple as a comma-separated string (x, y, z)."""
    x, y, z = coord
    return f"{x}, {y}, {z}"


def print_error_details(error: Exception) -> None:
    """Print structured details (type and args) for a caught exception."""
    print(
        f"{C.BG_RED}Error details:{C.RESET}\n"
        f"{C.RED}Type:{C.RESET} {type(error).__name__}\n"
        f"{C.RED}Args:{C.RESET} {error.args}"
        )


def coordinate_parsing() -> tuple[int, int, int]:
    """Parse 3 integer coordinates from sys.argv and return them as a tuple."""
    if len(sys.argv) != 4:
        raise ValueError(
            f"Bad input, cannot process. "
            f"Please provide 3 integer values as coordinates.\n"
            f"{C.YELLOW}Example usage: python3 {sys.argv[0]} "
            f"<coordinate1> <coordinate2> <coordinate3>{C.RESET}"
            )

    x2 = int(sys.argv[1])
    y2 = int(sys.argv[2])
    z2 = int(sys.argv[3])

    return (x2, y2, z2)


def coordinate_creation(coord1: tuple[int, int, int],
                        coord2: tuple[int, int, int]) -> None:
    """Print the created position and its distance to the reference
    coordinate."""
    print(
        f"{C.YELLOW}Position created:{C.RESET} {coord2}\n"
        f"{C.YELLOW}Distance between {coord1} and {coord2}:{C.RESET} "
        f"{calculate_distance(coord1, coord2)}\n"
        )


def calculate_distance(coord1: tuple[int, int, int],
                       coord2: tuple[int, int, int]) -> float:
    """Return the Euclidean distance between two 3D coordinates
    (rounded to 2 decimals)."""
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    distance = round(
        math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2), 2
        )
    return distance


def valid_parsing_demo(coord1: tuple[int, int, int],
                       coord2: tuple[int, int, int]) -> None:
    """Display the formatted parsing result for a valid coordinate tuple."""
    unpacked = coordtinate_tuple_unpack(coord2)
    print(
        f"{C.YELLOW}Parsing valid coordtinates:{C.RESET} \"{unpacked}\"\n"
        f"{C.YELLOW}Parsed position:{C.RESET} {coord2}\n"
        f"{C.YELLOW}Distance between {coord1} and {coord2}:{C.RESET} "
        f"{calculate_distance(coord1, coord2)}\n"
        )


def invalid_parsing_demo(coord1: tuple[int, int, int],
                         unpacked: str) -> None:
    """Attempt to parse invalid coordinates and demonstrate graceful error
    output."""
    print(
        f"{C.RED}Parsing invalid coordinates:{C.RESET} \"{unpacked}\"")
    try:
        cml_args = unpacked.split(",")
        if len(cml_args) != 3:
            raise ValueError(f"Program expects 3 values, got {len(cml_args)}")
        coordinates = (int(cml_args[0]), int(cml_args[1]), int(cml_args[2]))
        valid_parsing_demo(coord1, coordinates)
    except Exception as e:
        print(f"{C.RED}Error parsing coordinates:{C.RESET} {e}\n")
        print_error_details(e)


def main() -> None:
    """Run the coordinate system demonstration using command-line input."""
    print(f"{C.BLUE}=== Game Coordinate System ==={C.RESET}")
    coord1 = (0, 0, 0)

    # Parse user-provided coordinates from command-line arguments
    coord2 = coordinate_parsing()

    # Display coordinate creation and distance calculation
    coordinate_creation(coord1, coord2)

    # Demonstrate valid parsing output
    valid_parsing_demo(coord1, coord2)

    # Demonstrate invalid parsing scenario with mock data
    invalid_parsing_demo(coord1, "abc, def, hgi")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{C.BG_RED}Error:{C.RESET} {e}")
