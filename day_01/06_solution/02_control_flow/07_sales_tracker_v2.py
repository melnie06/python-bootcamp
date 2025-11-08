# Ask the user how many items will be calculated
input_count = int(input("Enter count of items: "))
total = 0

# Use a for loop to ask for more than one cost and count
for number in range(1, input_count + 1):
    item_cost = int(input(f"Enter item {number} cost: "))
    item_count = int(input(f"Enter item {number} count: "))
    item_total = item_cost * item_count

    total += item_total

print(total)
