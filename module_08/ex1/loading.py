#!/usr/bin/env python3


"""
Check external Python dependencies and simulate Matrix data analysis.

This script demonstrates how Python projects can depend on external libraries
such as numpy, pandas, and matplotlib.

The program first checks whether the required libraries are installed. If they
are available, it generates a fake dataset, processes it, and creates a graph
image.

This exercise also demonstrates why dependency management tools such as pip,
requirements.txt, and Poetry are important in real projects.
"""


# importlib allows importing modules dynamically using their names.
import importlib


class C:
    """ANSI color codes used to make terminal output easier to read."""

    RESET = "\033[0m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    PURPLE = "\033[35m"
    BG_RED = "\033[41m"


def dependency_validation(name: str, use: str) -> bool:
    """Check whether a dependency is installed and available.

    The function tries to import the module dynamically using its string name.
    If the import succeeds, the dependency is ready. Otherwise, an ImportError
    exception is raised and handled.

    Args:
        name: Name of the Python package to test.
        use: Short description of what the package is used for.

    Returns:
        True if the package is installed, otherwise False.
    """

    # Try importing the package dynamically from its string name.
    try:
        # Read the package version if available.
        version_no = getattr(module_name, "__version__", "unknown")
        module_name = importlib.import_module(name)
        print(f"{C.GREEN}[ OK ]{C.RESET} {name} ({version_no}) - {use} ready")
        return True

    # ImportError happens when the package is not installed.
    except ImportError:
        print(f"{C.RED}Missing {name}{C.RESET} - install it with:\n"
              f"{C.YELLOW}pip install -r requirements.txt{C.RESET}\n"
              f"or {C.YELLOW}poetry install{C.RESET}\n")
        return False


def main() -> None:
    """Run dependency checks and perform a simple data analysis.

    The workflow of the program is:
    1. Check external dependencies
    2. Stop safely if a dependency is missing
    3. Generate random data using numpy
    4. Organize data using pandas
    5. Create and save a graph using matplotlib
    """
    print(f"{C.BLUE}LOADING STATUS: Loading programs...\n"
          f"Checking dependencies:\n")

    # Each tuple contains a package name and its purpose in the project.
    dependencies = [("pandas", "Data manipulation"),
                    ("numpy", "Numerical computation"),
                    ("matplotlib", "Visualization")]

    # This variable tracks whether all required imports are available.
    ready_imports = True

    # Test every required dependency one by one.
    for name, use in dependencies:
        if not dependency_validation(name, use):
            ready_imports = False

    # Stop the program if at least one dependency is missing.
    if not ready_imports:
        print("Some programs failed to load."
              "Install dependencies and try again.")
        return

    print("\nAnalyzing Matrix data...")

    # External libraries are imported only after validation succeeds.
    import numpy
    import pandas
    import matplotlib.pyplot

    # Number of random values that will be generated.
    data_points = 1000
    print(f"Processing {data_points} data points...")

    # Generate random integer data between 0 and 100.
    # numpy is used here as the source of the dataset.
    matrix_signal = numpy.random.randint(0, 100, data_points)

    # Store the generated data inside a pandas DataFrame.
    df = pandas.DataFrame({
        "signal_strength": matrix_signal
    })

    print("Generating visualization...")

    # Create a new graph figure before plotting the data.
    matplotlib.pyplot.figure()

    # Draw the signal values as a line graph.
    matplotlib.pyplot.plot(df["signal_strength"], color="purple")
    matplotlib.pyplot.title("Matrix Signal Analysis Graph", color="blue")
    matplotlib.pyplot.xlabel("Data point", color="grey")
    matplotlib.pyplot.ylabel("Signal strength", color="grey")

    # Display grid lines to improve graph readability.
    matplotlib.pyplot.grid(True)

    # Save the generated graph as an image file.
    matplotlib.pyplot.savefig("matrix_analysis.png")

    # Close the figure to free resources after saving.
    matplotlib.pyplot.close()

    print("\nAnalysis complete!")
    print(f"{C.YELLOW}Results saved to:{C.RESET} matrix_analysis.png")


if __name__ == "__main__":
    main()
