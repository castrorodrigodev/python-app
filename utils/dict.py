# capital_dict = {
#     "Argentina": "Buenos Aires",
#     "Espala": "Madrid",
#     "Italia": "Roma",
#     "Brasil": "Brazilia",
#     "Inglaterra": "Londres",
# }

# print(capital_dict)

# capital_dict["Inglaterra"] = "LONDRESSS"
# print(capital_dict)

# capital_dict["Inglaterraa"] = 1
# print(capital_dict)

# del capital_dict["Inglaterraa"]
# print(capital_dict)

# print(capital_dict.keys())
# print(capital_dict.values())
# print(len(capital_dict))

# for key in cities:
#     value = cities[key]
#     print(key, value)

# for key, value in cities.items():
#     print(f"Key: {key} -> Value: {value}")


def get_dict_keys(my_dict):
    return my_dict.keys()


def get_dict_values(my_dict):
    return my_dict.values()


def get_dict_items(my_dict):
    return my_dict.items()


def get_dict_size(my_dict):
    return len(my_dict)


def custom_set_default(my_dict, key, default_value):
    value = my_dict.setdefault(key, default_value)
    return (my_dict, value)
