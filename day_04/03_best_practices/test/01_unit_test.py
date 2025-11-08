def square(x):
	return x * x


def test_square_positive():
	assert square(2) == 4


def test_square_negative():
	assert square(-3) == 9


def test_square_zero():
	assert square(0) == 0
