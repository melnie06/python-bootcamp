orders = {}

order = input("Enter order: ")
while order:
    count = int(input("Enter how many: "))
    order = input("Enter order: ")

    if order in orders:
        orders[order] += count
    else:
        orders[order] = count

print(orders)
