# Basic type hinting
counter: int = 1

# List of int's
numbers: list[int] = [1, 2, 3]

# Dictionary with str keys and int for values
months: dict[str, int] = {"Jan": 1, "Feb": 2, "Mar": 3}

# Dictionary str keys and list of int for values
tasks: dict[str, list[int]] = {"dev": [1, 2, 3], "test": [4]}

# Tuple with two int (fixed size and data types)
point: tuple[int, int] = (0, 1)

# List of tuples with two int
points: list[tuple[int, int]] = [(9, 1), (2, 3), (5, 2)]
