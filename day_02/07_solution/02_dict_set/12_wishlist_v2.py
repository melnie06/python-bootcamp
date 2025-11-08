# Fill in the details of the item you plan to buy
wishlist = [
    {
        'Name': 'Smartphone',
        'Info': 'Latest model smartphone',
        'Price': 70_000.00,
        'Stock': 25,
    },
    {
        'Name': 'Laptop',
        'Info': 'Latest model laptop',
        'Price': 100_000.00,
        'Stock': 10,
    },
    {
        'Name': 'Headset',
        'Info': 'Latest model headset',
        'Price': 10_000.00,
        'Stock': 3,
    },
]

# Print the item details in the following format:
for order in wishlist:
    print("Order:")
    for key, value in order.items():
        print(f"\t{key}:\t{value}")
