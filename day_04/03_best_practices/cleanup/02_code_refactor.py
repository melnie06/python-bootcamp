def count_per_item(items):
    item_count = {}

    for item in items:

        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    return item_count


