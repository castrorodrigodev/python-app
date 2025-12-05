from utils.math import addition, even_number


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0


def test_even_number():
    assert even_number(4) is True
    assert even_number(5) is False
