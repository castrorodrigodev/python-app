from utils.lists import size


def test_list_size():
    users = ["Rodrigo", "Fernando", "Giovani", "Damaris"]
    assert size(users) == 4
    assert size([]) == 0
    assert users[-1] == "Damaris"
    assert size(users[0:3]) == 3
