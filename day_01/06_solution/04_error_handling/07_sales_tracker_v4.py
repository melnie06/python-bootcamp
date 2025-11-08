def get_number(instructions):
    invalid = True

    while invalid:
        number = input("Enter item cost: ")

        try:
            number = int(number)

            if number < 0:
                raise ValueError()

            invalid = False

        except ValueError:
            print("Input not a positive number. Try again.")

    return number


def add(total):
    item_cost = get_number("Enter item cost: ")
    item_count = get_number("Enter item count: ")
    total_item_cost = item_cost * item_count
    return total + total_item_cost


def sub(total):
    """Remove total item cost (cost, count) from total and return"""
    item_cost = get_number("Enter item cost: ")
    item_count = get_number("Enter item count: ")
    total_item_cost = item_cost * item_count
    return total - total_item_cost


def show(total):
    """Print total"""
    print("Total:", total)


def main():
    total = 0
    running = True
    while running:
        command = input("Provide command: ")
        if command == "add":
            total = add(total)
        elif command == "sub":
            total = sub(total)
        elif command == "show":
            show(total)
        elif command == "exit":
            running = False


main()
