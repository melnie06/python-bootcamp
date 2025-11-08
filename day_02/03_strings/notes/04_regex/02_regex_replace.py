import re

text = "Alice has an apple and an avocado."
pattern = r"\ba\w*"
result = re.sub(pattern, "X", text)

print(result)
