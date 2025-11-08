items = ["rice", "noodles", "toyo", "coffee"]
item_to_find = "spam"

for item in items:
    print(item)

    if item == item_to_find:
        item_found = True
        break
print('Item found: ', item_found)
        # print('not {item_to_find}')#   # print and exit loop



# for number in range (1, 100 + 1):
#     #skip 21 -> 79
#     if 21 <= number <= 79:
#         continue
#     print(number)