total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        number = int(input("Enter a number: "))
        total += number
        print("Current total is:", total)
    if command == "sub":
        number = int(input("Enter a number: "))
        total -= number
        print("Current total is:", total)
    elif command == "exit":
        running = False
