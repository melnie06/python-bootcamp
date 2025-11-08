# String to int
num_str = "42"
print(int(num_str))  # 42

# Float to int (truncates, not rounds!)
num_float = 3.99
print(int(num_float))  # 3

# Boolean to int
print(int(True))  # 1
print(int(False))  # 0

# Binary/hex string to int
print(int("1010", 2))  # 10
print(int("FF", 16))  # 255
