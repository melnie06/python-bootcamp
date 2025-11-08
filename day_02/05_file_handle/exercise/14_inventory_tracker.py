def add(inventory):
    item_name = input("Item name: ")
    item_info = input("Item info: ")

    item = {"Name": item_name, "Info": item_info}
    inventory.append(item)

    print(f"{item} added to inventory\n")


def remove(inventory):
    index = int(input("Index (remove): "))
    removed_item = inventory.pop(index)
    print(f"{removed_item} removed from inventory\n")


def read(inventory):
    index = int(input("Index (read): "))
    item = inventory[index]
    print(f"Item {index}: {item}\n")


def show(inventory):
    if not inventory:
        print("Inventory is empty.\n")
        return

    for number, info_detail in enumerate(inventory, start=1):
        print(f"Item {number}:")

        for key, value in info_detail.items():
            print(f"\t{key}: {value}")


def save(inventory):
    """Save the inventory to a JSON file"""


def load(inventory):
    """Return the inventory from a JSON file"""
    return []


def main():
    running = True
    item_detail = str | int | float
    inventory: list[dict[str, item_detail]] = []

    while running:
        command = input("Command: ").strip().lower()

        if command == "add":
            add(inventory)

        elif command == "remove":
            remove(inventory)
        elif command == "read":
            read(inventory)
        elif command == "show":
            show(inventory)
        elif command == "save":
            save(inventory)
        elif command == "load":
            inventory = load(inventory)
        elif command == "exit":
            running = False
            print("Exiting...")


main()
