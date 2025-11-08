class NotANumberError(Exception):
    pass


class NotPositiveError(Exception):
    pass


class OutOfRangeError(Exception):
    pass


number = input("Enter positive number [1,100]: ")

try:
    if not number.isdigit():
        raise NotANumberError("Input is not a number.")

    number = int(number)

    if number <= 0:
        raise NotPositiveError("Number is not positive.")

    if not (1 <= number <= 100):
        raise OutOfRangeError("Number not in range [1, 100].")

    print(f"Valid number: {number}")

except (NotANumberError, NotPositiveError, OutOfRangeError) as e:
    print(f"Invalid input: {e}")
