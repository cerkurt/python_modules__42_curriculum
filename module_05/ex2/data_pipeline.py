#!/usr/bin/env python3

"""
Data Pipeline Module

This module builds a small data pipeline system.
Different processors can validate and store different types of data, and export
plugins can format processed output.

Included processors:
- NumericProcessor: handles numbers
- TextProcessor: handles strings
- LogProcessor: handles log dictionaries
"""

from abc import ABC, abstractmethod
from typing import Any, Protocol


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

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if this processor can handle the data."""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Store valid data inside the processor."""

    def _store_item(self, value: str) -> None:
        # Save value with current rank and update counters
        """Store one processed value."""
        self._stored_data.append((self._next_rank, value))
        self._next_rank += 1
        self.total_processed += 1

    def output(self) -> tuple[int, str]:
        """Return one stored item using FIFO order."""
        # Return and remove the oldest stored item
        if not self._stored_data:
            raise ValueError(
                f"{C.RED}No data available in processor.{C.RESET}")
        return self._stored_data.pop(0)

    def remaining_items(self) -> int:
        """Return the number of stored items."""
        return len(self._stored_data)


class NumericProcessor(DataProcessor):
    """Processor for numeric data."""

    def validate(self, data: Any) -> bool:
        # Accept a single number or a list containing only numbers
        if isinstance(data, (int, float)):
            return True
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
        # Accept a single string or a list containing only strings
        if isinstance(data, str):
            return True
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


class ExportPlugin(Protocol):
    """Protocol used by export plugins."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Receive exported processor data."""


class CSVExportPlugin:
    """Export data in CSV format."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        # Extract only values and join them with commas
        print("CSV Output:")
        values = []
        for _, value in data:
            values.append(value)
        print(",".join(values))


class JSONExportPlugin:
    """Export data in a simple JSON-like format."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        # Build key-value pairs using rank and value
        print(f"{C.PURPLE}JSON Output:{C.RESET}", end=' ')
        parts = []
        for rank, value in data:
            parts.append(f'"item_{rank}": "{value}"')
        print("{" + ", ".join(parts) + "}")


class DataStream:
    """Routes data to processors and exports processed output."""

    def __init__(self) -> None:
        # Keeps processors in registration order
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Register a processor for future stream data."""
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Send each stream element to a matching processor."""
        for element in stream:
            # Try processors one by one until one accepts the element
            handled = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    handled = True
                    break
            # Print an error if no processor accepted the element
            if not handled:
                print(
                    f"{C.BG_RED}DataStream error{C.RESET} - "
                    f"{C.RED}Can't process element in stream:{C.RESET} "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        """Print total and remaining item counts for each processor."""
        print(f"{C.GREEN}== DataStream statistics =={C.RESET}")
        if not self.processors:
            print(f"{C.RED}No processor found, no data{C.RESET}")
            return

        # Show stats for every registered processor
        for processor in self.processors:
            name = processor.__class__.__name__.replace(
                "Processor",
                " Processor",
            )
            print(
                f"{C.PURPLE}{name}{C.RESET}:"
                f" total {processor.total_processed} items processed, "
                f"remaining {processor.remaining_items()} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Collect processed data and send it to an export plugin."""
        for processor in self.processors:
            # Collect a limited number of items from each processor
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                if processor.remaining_items() == 0:
                    break
                collected.append(processor.output())
            # Send collected data to the selected plugin
            plugin.process_output(collected)


def main() -> None:
    """Run a simple demonstration of the data pipeline."""
    # Create processors and export plugins
    data_stream = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    csv_plugin = CSVExportPlugin()
    json_plugin = JSONExportPlugin()

    # First mixed batch of test data
    first_batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            }
        ],
        42,
        ["Hi", "five"]
    ]

    # Second mixed batch of test data
    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    # Show initial state before processing
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    print()
    data_stream.print_processors_stats()
    print()

    # Register all processors
    print("Registering Processors")
    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)
    print()

    # Process the first batch
    print(f"{C.YELLOW}Send first batch of data on stream:{C.RESET} "
          f"{first_batch}")
    print()
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()
    print()

    # Export some processed items using CSV format
    print(f"{C.YELLOW}Send 3 processed data from each processor "
          f"to a CSV plugin:{C.RESET}")
    data_stream.output_pipeline(3, csv_plugin)
    print()
    data_stream.print_processors_stats()
    print()

    # Process another batch of data
    print(f"{C.YELLOW}Send another batch of data:{C.RESET} {second_batch}")
    print()
    data_stream.process_stream(second_batch)
    data_stream.print_processors_stats()
    print()

    # Export processed items using JSON format
    print(f"{C.YELLOW}Send 5 processed data from each processor "
          f"to a JSON plugin:{C.RESET}")
    data_stream.output_pipeline(5, json_plugin)
    print()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
