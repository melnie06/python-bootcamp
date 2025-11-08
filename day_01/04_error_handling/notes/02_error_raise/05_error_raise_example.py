try:
    user_input = int(input("Enter Number: "))
    if user_input < 0:
        raise ValueError()

except ValueError:
    print("We don’t accept strings or negatives!")
