#!/usr/bin/env python3
"""
Garden introduction script.

This script demonstrates:
- running a Python script
- defining a main() function
- using variables to store data
- printing formatted output to the terminal
"""


def main():
    """Program entry point.

    Stores simple plant information in variables and prints it
    to the terminal in a readable format.
    """
    # Store basic plant data in variables
    name = "Rose"
    height = "25cm"
    age = "30 days"
    # Display a simple header
    print("=== Welcome to My Garden ===")
    # Print plant information line by line
    print("Plant:", name)
    print("Height:", height)
    print("Age:", age)


# This special check ensures main() runs only when this file is executed
# directly
if __name__ == "__main__":
    main()
