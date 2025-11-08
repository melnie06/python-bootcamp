with open("test.txt", "w") as file:
    lines = [1, 2, 3]
    lines = [str(line) + "\n" for line in lines]
    file.writelines(lines)
