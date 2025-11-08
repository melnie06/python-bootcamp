# Ask the cost and pax or count for three separate items
item_cost_1 = int(input("Item cost 1: "))
item_count_1 = int(input("Item count 1: "))

item_cost_2 = int(input("Item cost 2: "))
item_count_2 = int(input("Item count 2: "))

item_cost_3 = int(input("Item cost 3: "))
item_count_3 = int(input("Item count 3: "))

# Calculate the total
total = (
        (item_cost_1 * item_count_1)
        + (item_cost_2 * item_count_2)
        + (item_cost_3 * item_count_3)
)
print(total)
