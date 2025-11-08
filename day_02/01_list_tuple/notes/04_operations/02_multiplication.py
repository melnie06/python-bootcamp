numbers_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_cards = ["+2", "skip", "reverse"]
super_cards = ["0", "+4", "color"]

max_cards = 8 * (special_cards + numbers_cards)
min_cards = 4 * super_cards

print(max_cards + min_cards)
