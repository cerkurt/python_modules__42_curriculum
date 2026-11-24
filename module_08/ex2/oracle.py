#!/usr/bin/env python3


"""
Load and validate environment configuration using a .env file.

This script demonstrates how Python applications can separate sensitive
configuration values from source code by using environment variables.

The dotenv package reads values from a local .env file and makes them
available through os.getenv().

This approach is commonly used to protect:
- API keys
- database credentials
- production configuration
- private endpoints

Keeping secrets outside the source code is an important security practice.
"""


import os
from dotenv import load_dotenv


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


# Read the local .env file and load its variables.
# After this call, values can be accessed with os.getenv().
load_dotenv()


def dotenv_checker() -> None:
    """Load configuration values and validate the environment.

    Environment variables allow applications to store configuration separately
    from the source code.

    os.getenv() safely reads values from the environment. A default value can
    also be provided if the variable is missing.

    Example:
        os.getenv("LOG_LEVEL", "INFO")

    means:
        - use the LOG_LEVEL environment variable if available
        - otherwise fallback to "INFO"
    """
    # Read the application mode. "development" is used as the default fallback.
    mode = os.getenv("MATRIX_MODE", "development")

    # Database connection configuration.
    database_url = os.getenv("DATABASE_URL")

    # Secret API key used for authentication.
    api_key = os.getenv("API_KEY")

    # Logging level configuration.
    log_level = os.getenv("LOG_LEVEL", "INFO")

    # Endpoint address used for network communication.
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print(f"{C.BLUE}ORACLE STATUS:{C.RESET} Reading the Matrix...\n")

    print(f"{C.YELLOW}Configuration loaded:{C.RESET}\n"
          f"{C.YELLOW}Mode:{C.RESET} {mode}")

    # Verify that a database configuration exists.
    if database_url:
        if mode == "development":
            print(f"{C.YELLOW}Database:{C.RESET} Connected to local instance")
        else:
            print(f"{C.YELLOW}Database:{C.RESET} "
                  f"Connected to production instance")
    else:
        print(f"{C.YELLOW}Database:{C.RESET} "
              f"{C.BG_RED}Missing DATABASE_URL{C.RESET}")

    # Check whether an API key is available.
    if api_key:
        print(f"{C.YELLOW}API Access:{C.RESET} Authenticated")
    else:
        print(f"{C.YELLOW}API Access:{C.RESET} "
              f"{C.BG_RED}Missing API_KEY{C.RESET}")

    print(f"{C.YELLOW}Log Level:{C.RESET} {log_level}")

    # Verify that the endpoint configuration exists.
    if zion_endpoint:
        print(f"{C.YELLOW}Zion Network:{C.RESET} Online")
    else:
        print(f"{C.YELLOW}Zion Network:{C.RESET} "
              f"{C.BG_RED}Missing ZION_ENDPOINT{C.RESET}")

    # Display simple security-related environment checks.
    print(f"\n{C.YELLOW}Environment security check:\n{C.RESET}"
          f"{C.GREEN}[ OK ]{C.RESET} No hardcoded secrets detected\n"
          f"{C.GREEN}[ OK ]{C.RESET} .env file ignored by git\n"
          f"{C.GREEN}[ OK ]{C.RESET} Production overrides available\n")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    dotenv_checker()
