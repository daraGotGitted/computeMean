def parseNotes(gradeInput: str) -> list[float]:
    """
    Converts a string of notes separated into spaces/commas into an array of floats.

    Args:
        noteInput (str): grades string (example. "7, 8.5, 9").

    Returns:
        list[float]: Array of floats containing grades.

    Raises:
        ValueError: If any of the grades cannot be converted into float.
    """

    # Replaces commas into spaces and then splits into an array separated by spaces.
    parts = gradeInput.replace(",", " ").split()
    return [float(p) for p in parts]


def meanCalc(grades: list[float]) -> float:
    """
    Calculate arithmetic mean given an array of floats.

    Args:
        grades (list[float]): Array of floats.

    Returns:
        float: Grades mean.

    Raises:
        ValueError: If array is empty.
    """

    # Raises error if no grades were inputted.
    if not grades:
        raise ValueError("Grades array is empty.")
    return sum(grades) / len(grades)


def main() -> None:
    """
    Asks the user for grades and display them in console.
    """

    #Ask user for grades.
    gradeInput = input("Input noted separated by commas/spaces: ")
    try:
        grades = parseNotes(gradeInput)
        mean = meanCalc(grades)
        print(f"Mean: {mean:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
