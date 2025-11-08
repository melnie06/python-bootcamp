def add(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total + total_item_cost


def sub(total):
    """TODO:
        Ask for an item_cost
        Ask for an item_count
        Calculate the total_item_cost
        return the total - total_item_cost"""


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


main()
