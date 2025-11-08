wishlist = [
    {
        'Name': 'Smartphone',
        'Info': 'Latest model smartphone',
        'Price': 70_000.00,
        'Stock': 25
    },
    {
        'Name': 'Wireless Headphones',
        'Info': 'Noise-canceling headphones',
        'Price': 10_000.00,
        'Stock': 50
    },
]

for order in wishlist:
    print("Order:")
    print("\t Item:", order['Name'])
    print("\t Info:", order['Info'])
    print("\t Stock:", order['Price'])
    print("\t Price:", order['Stock'])
    print()
