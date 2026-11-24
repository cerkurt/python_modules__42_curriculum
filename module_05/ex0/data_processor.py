#!/usr/bin/env python3

"""
Data Processor Module

This module demonstrates a simple polymorphic data processing system.
Different processors can validate, store, and output different types of data.

Included processors:
- NumericProcessor: handles numbers
- TextProcessor: handles strings
- LogProcessor: handles log dictionaries

Polymorphism: different objects responding differently to the same method call.

- Same method name. but different behavior.
"""

from abc import ABC, abstractmethod
from typing import Any


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


class DataProcessor(ABC):
    """Base abstract class for all data processors."""

    def __init__(self) -> None:
        # Stores processed data as (rank, value)
        # Rank keeps insertion order
        self._stored_data: list[tuple[int, str]] = []
        # Counter used to assign ranks
        self._next_rank: int = 0
        # Counts all processed items
        self.total_processed: int = 0

    # Kind of a contract: “If you want to become a DataProcessor, you MUST
    # provide these methods.”

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # Must be implemented by subclasses to check data compatibility.
        # Every subclass MUST implement validate()
        """Check if this processor can handle the data."""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        # Must be implemented by subclasses to store validated data
        # Every subclass MUST implement ingest()
        """Store valid data inside the processor."""

    def _store_item(self, value: str) -> None:
        # Save value with current rank and update counters
        """Store one processed value."""
        self._stored_data.append((self._next_rank, value))
        self._next_rank += 1
        self.total_processed += 1

    def output(self) -> tuple[int, str]:
        # Return and remove the oldest stored item
        """Return one stored item using FIFO order."""
        if not self._stored_data:
            raise ValueError(
                f"{C.RED}No data available in processor.{C.RESET}")
        return self._stored_data.pop(0)

    def remaining_items(self) -> int:
        # Return how many items are still stored
        """Return the number of stored items."""
        return len(self._stored_data)


class NumericProcessor(DataProcessor):
    """Processor for numeric data."""

    def validate(self, data: Any) -> bool:
        # Accept a single number
        if isinstance(data, (int, float)):
            return True
        # Accept lists containing only numbers
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        # Stop if invalid data is given
        if not self.validate(data):
            raise ValueError(f"{C.RED}Improper numeric data.{C.RESET}")
        # Store every number as a string
        if isinstance(data, list):
            for item in data:
                self._store_item(str(item))
        else:
            self._store_item(str(data))


class TextProcessor(DataProcessor):
    """Processor for text data."""

    def validate(self, data: Any) -> bool:
        # Accept a single string
        if isinstance(data, str):
            return True
        # Accept lists containing only strings
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        # Stop if invalid data is given
        if not self.validate(data):
            raise ValueError(f"{C.RED}Improper text data.{C.RESET}")
        # Store text values directly
        if isinstance(data, list):
            for item in data:
                self._store_item(item)
        else:
            self._store_item(data)


class LogProcessor(DataProcessor):
    """Processor for log dictionary data."""

    def validate(self, data: Any) -> bool:
        # Accept one valid log dictionary or a list of them
        if isinstance(data, dict):
            return self._is_valid_log_dict(data)
        if isinstance(data, list):
            return all(self._is_valid_log_dict(item) for item in data)
        return False

    def _is_valid_log_dict(self, data: Any) -> bool:
        # Check required keys and value types
        if not isinstance(data, dict):
            return False
        if "log_level" not in data or "log_message" not in data:
            return False
        return isinstance(data["log_level"], str) and isinstance(
            data["log_message"], str
        )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        # Stop if invalid log data is given
        if not self.validate(data):
            raise ValueError(f"{C.RED}Improper log data.{C.RESET}")
        # Convert logs into readable strings before storing
        if isinstance(data, list):
            for item in data:
                self._store_item(
                    f"{item['log_level']}: {item['log_message']}"
                )
        else:
            self._store_item(
                f"{data['log_level']}: {data['log_message']}"
            )


def test_numeric_processor() -> None:
    """Test NumericProcessor behavior."""
    processor = NumericProcessor()

    print(f"{C.YELLOW}Testing Numeric Processor...{C.RESET}\n"
          f"Trying to validate input {C.YELLOW}'42'{C.RESET}: "
          f"{processor.validate(42)}\n"
          f"Trying to validate input {C.YELLOW}'Hello'{C.RESET}: "
          f"{processor.validate('Hello')}")

    print(f"Test invalid ingestion of string {C.BG_RED}'foo'{C.RESET} without "
          f"prior validation:")
    try:
        processor.ingest("foo")
    except ValueError as exc:
        print(f"{C.BG_RED}Got exception:{C.RESET} {exc}")

    print(f"{C.YELLOW}Processing data:{C.RESET} [1, 2, 3, 4, 5]")
    processor.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = processor.output()
        print(f"Numeric value {C.YELLOW}{rank}{C.RESET}: {value}")
    print()


def test_text_processor() -> None:
    """Test TextProcessor behavior."""
    processor = TextProcessor()

    print(f"{C.YELLOW}Testing Text Processor...{C.RESET}\n"
          f"Trying to validate input {C.YELLOW}'42'{C.RESET}: "
          f"{processor.validate(42)}\n"
          f"{C.YELLOW}Processing data:{C.RESET} ['Hello', 'Nexus', 'World']")
    processor.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = processor.output()
    print(f"Text value {C.YELLOW}{rank}{C.RESET}: {value}")
    print()


def test_log_processor() -> None:
    """Test LogProcessor behavior."""
    processor = LogProcessor()
    logs = [{"log_level": "NOTICE", "log_message": "Connection to server"},
            {"log_level": "ERROR", "log_message": "Unauthorized access!!"}]

    print(f"{C.YELLOW}Testing Log Processor...{C.RESET}\n"
          f"Trying to validate input {C.YELLOW}'Hello'{C.RESET}: "
          f"{processor.validate('Hello')}")
    print(f"{C.YELLOW}Processing data:{C.RESET} {logs}")
    processor.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = processor.output()
        print(f"Log entry {C.YELLOW}{rank}{C.RESET}: {value}")
    print()


def main() -> None:
    """Run all processor demonstrations."""
    print(f"{C.BLUE}=== Code Nexus - Data Processor ==={C.RESET}\n")
    test_numeric_processor()
    test_text_processor()
    test_log_processor()


if __name__ == "__main__":
    main()
