# Tuples

# personal_data = ("Rodrigo", 1988, 1, 21, "Rodrigo")
# print("TUPLE: ", personal_data)
# print("TUPLE LIST: ", list(personal_data))
# print("TUPLE LIST TUPLE: ", tuple(list(personal_data)))
# print(1988 in personal_data)
# print(1989 in personal_data)
# print("Rodrigo" in personal_data)
# print("rodrigo" in personal_data)
# print(personal_data.count("Rodrigo"))
# print(personal_data.count("Rodrigo1"))
# # print(personal_data.count()) -- Error
# print(len(personal_data))


def tuple_length(tuple):
    return len(tuple)


def tuple_include_value(tuple, value):
    return value in tuple

def tuple_existences_value(tuple, value):
    return tuple.count(value)
