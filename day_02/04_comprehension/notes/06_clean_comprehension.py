def process(number):
    return ((1 + number) // 2) ** 3


def condition(number):
    return number > 10


numbers = [991, 12, 89, 34, 121, 0]
data = [process(num) for num in numbers if condition(num)]
print(data)
