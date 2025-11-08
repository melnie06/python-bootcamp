def add(a, b):
    return a + b

def square(x):
    return x * x

def multiply(a, b):
    return a * b

def calculate_expression(x, y, z=0):
    return add(square(x), multiply(y, 2)) - z

def test_calculate_expression():
    assert calculate_expression(2, 3) == 10


def test_calculate_expression_three_inputs():
    assert calculate_expression(2, 3, 2) == 8
