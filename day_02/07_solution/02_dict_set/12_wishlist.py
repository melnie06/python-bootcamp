# Fill in the details of the item you plan to buy
order = {
    'Name': 'Smartphone',
    'Info': 'Latest model smartphone',
    'Price': 70_000.00,
    'Stock': 25,
}

# Print the item details in the following format:
print("Order:")
for key, value in order.items():
    print(f"\t{key}:\t{value}")
