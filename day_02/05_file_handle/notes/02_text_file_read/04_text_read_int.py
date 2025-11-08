with open("test.txt", "r") as file:
    numbers = [int(line) for line in file.read().splitlines()]
