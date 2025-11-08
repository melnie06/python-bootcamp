def positive_input():
    while True:
        number = input("Enter number: ")

        try:
            number = int(number)

            if number < 0:
                raise ValueError("Number cannot be negative.")

            return number

        except ValueError:
            print("Please enter a positive number.")


positive_input()
print("Entered:", positive_input())
