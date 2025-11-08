def add(total):
    """TODO: Add item cost (cost, count) from total and return"""


def sub(total):
    """TODO: Remove item cost (cost, count) from total and return"""


def show(total):
    """TODO: Print total"""


def main():
    total = 0
    running = True
    while running:
        command = input("Provide command: ")
        if command == "command 1":
            total = add(total)
        elif command == "exit":
            running = False
