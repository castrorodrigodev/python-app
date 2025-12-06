from utils.tuples import tuple_length, tuple_include_value, tuple_existences_value

personal_data = ("Rodrigo", 1988, 1, 21, "Rodrigo")


def test_tuple_length():
    assert tuple_length(personal_data) != 4
    assert tuple_length(personal_data) == 5
    assert tuple_length(personal_data) > 0


def test_tuple_include_value():
    assert tuple_include_value(personal_data, 1988) is True
    assert tuple_include_value(personal_data, 1989) is False


def test_tuple_existences_value():
    assert tuple_existences_value(personal_data, "Fernando") == 0
    assert tuple_existences_value(personal_data, "Rodrigo") == 2


def test_tuple_destructuring():
    name, year, month, day, fifth = personal_data
    assert name == "Rodrigo"
    assert year == 1988
    assert month == 1
    assert day == 21
