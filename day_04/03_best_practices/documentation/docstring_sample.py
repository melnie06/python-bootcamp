import math


def calculate_circle_area(radius):
    """
    Return the area of a circle with the given radius.

    Args:
            radius (float): Circle's radius. Must be non-negative.

    Returns:
            float: Area of the circle.

    Raises:
            ValueError: If radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    return math.pi * radius ** 2
