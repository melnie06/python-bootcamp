with open("test.txt", "w") as file:
    lines = ["Line 1", "Line 2", "Line 3"]
    lines = [line + "\n" for line in lines]
    file.writelines(lines)
