import re

# You can use a custom input
s = "I like apple pie; pineapple is good too, apple is my favorite fruit."

# Replace every instance of "apple" with "buko"
print(re.sub(r'\bapple\b', 'buko', s))

# I like buko pie; pineapple is good too, buko is my favorite fruit.
