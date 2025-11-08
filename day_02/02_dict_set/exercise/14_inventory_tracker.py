def add(inventory):
    """TODO:
        Ask for item name, info, and stock
        Create a dictionary with key: name, info, stock
        Add that dictionary to inventory
    """


def remove(inventory):
    """TODO:
        Ask for item index (int)
        Remove item in that index in inventory
    """


def read(inventory):
    """TODO:
        Ask for item index (int)
                Show item in that index in inventory
    """
def show(inventory):
    """TODO: Print items line-by-line"""

def main():
    """Created to test functions"""
    running = True
    item_detail = str | int | float
    inventory: list[dict[str, item_detail]] = []

    while running:
        command = input("Command: ")
        if command == "add":
            # TODO: Use add command"""
            pass
        elif command == "remove":
            #  TODO: Use remove command"""
            pass
        elif command == "read":
            # TODO: Use read command"""
            pass
        elif command == "show":
            # TODO: Use show command"""
            pass
        elif command == "exit":
            running = False


main()
