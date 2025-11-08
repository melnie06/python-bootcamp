def square(x):
    return x * x


class TestSquareNumber:
    def test_square_positive(self):
        assert square(2) == 4

    def test_square_negative(self):
        assert square(-3) == 9


class TestSquareSpecial:
    def test_square_zero(self):
        assert square(0) == 0

    def test_square_increase(self):
        assert square(10) > 10
