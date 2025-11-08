def multiplication_table(x):
    for index in range(1, 10 + 1):
        print(f"{index} * {x} = {index * x}")

number = int(input("Pick a number: "))
multiplication_table(number)
