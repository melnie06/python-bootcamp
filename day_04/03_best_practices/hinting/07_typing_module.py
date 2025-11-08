from typing import Literal, Iterable

priority = Literal["low", "medium", "urgent"]
priorities: list[priority] = ["medium", "urgent", "urgent", "low"]


def urgent_points(items: Iterable) -> int:
    urgent_point: int = 10
    return sum(urgent_point for item in items if item == "urgent")
