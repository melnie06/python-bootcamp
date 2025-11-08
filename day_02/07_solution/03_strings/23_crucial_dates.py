import re

# You can use a custom input
s = "The event is on 12/15/2023, and the deadline is 01/01/2024."

# Print all the dates mentioned
print(re.findall(r"\d+/\d+/\d+", s))
