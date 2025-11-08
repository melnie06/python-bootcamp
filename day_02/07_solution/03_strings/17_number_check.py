# Ask the user for an input
user_input = input("Enter number: ")

if user_input.isnumeric():
    user_input = int(user_input)
    print(user_input + 1)
else:
    print("Please enter a valid number!")
