from utils.dict import get_dict_keys, get_dict_values, get_dict_size

capital_dict = {
    "Argentina": "Buenos Aires",
    "Espala": "Madrid",
    "Italia": "Roma",
    "Brasil": "Brazilia",
    "Inglaterra": "Londres",
}


def test_dict_keys():
    assert ("Argentina" in get_dict_keys(capital_dict)) is True


def test_dict_values():
    assert ("Buenos Aires" in get_dict_values(capital_dict)) is True
    assert ("Buenos aires" in get_dict_values(capital_dict)) is False


def test_dict_size():
    assert get_dict_size(capital_dict) != 4
    assert get_dict_size(capital_dict) == 5
