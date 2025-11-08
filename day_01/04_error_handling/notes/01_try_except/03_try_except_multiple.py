try:
    divider = int(input("Number: "))
    budget = 1_000
    print(budget / divider)
except ValueError:
    print("Enter a valid number!")
except ZeroDivisionError:
    print("Cannot pick zero")
