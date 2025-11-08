import re

text = "Call me at 123-456-7890"
numbers = re.findall(r"\d+", text)
print(numbers)
