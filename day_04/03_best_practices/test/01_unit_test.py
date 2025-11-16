def square(x):
	return x * x
	# if isinstance(x, str):
	# 	raise TypeError ('str')


# def test_square_string():
#     assert square(2)

def test_square_positive():
	assert square(2) == 4


def test_square_negative():
	assert square(-3) == 9


def test_square_zero():
	assert square(0) == 0
