# Dict with str keys and values that are either str, int, or float
UserData = dict[str, str | int | float]

users: list[UserData] = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
]
