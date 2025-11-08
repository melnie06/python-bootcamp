total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        user_input = int(input('Enter Number1: ')) # TODO: Ask for number
        total = (total + user_input)    # TODO: Add that number to the total
        print (f'Total running balance: {total}')# TODO: Print the current total
        # pass
    if command == "sub":
        user_input = int(input('Enter Number2: ')) 
        total = (user_input - total)    # TODO: Add that number to the total
        print (f'Total running balance: {total}')# TODO: Print the current total
        # pass
    elif command == "exit":
        running = False
