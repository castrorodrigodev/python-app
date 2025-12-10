# ************************ GENERATORS ************************
def generateNumberGn(limit):
    num = 1
    while num < limit:
        yield num * 2
        num = num + 1


# evenSeries = generateNumberGn(6)

# for i in evenSeries:
#     print(f"Element: {i}")

# print(next(evenSeries))
# print(next(evenSeries))
# print(next(evenSeries))
# print(next(evenSeries))
# print(next(evenSeries))


def cities_gn_1(*cities):
    for capital in cities:
        yield capital


def cities_gn_2(*cities):
    for capital in cities:
        for character in capital:
            yield character


def cities_gn_3(*cities):
    for capital in cities:
        yield from capital


# returned_cities = cities_gn_1("Berlin", "Roma", "Bogota", "Pekin", "Hanoi")

# print(next(returned_cities))  # Berlin
# print(next(returned_cities))  # Berlin, Roma
# print(next(returned_cities))  # Berlin, Roma, Bogota
# print(next(returned_cities))
# print(next(returned_cities))

returned_cities_2 = cities_gn_2(
    "Berlin", "Roma", "Bogota", "Pekin", "Hanoi"
)  # Similar to cities_gn_3
# print(next(returned_cities_2))  # B
# print(next(returned_cities_2))  # e
# print(next(returned_cities_2))  # r
# print(next(returned_cities_2))
# print(next(returned_cities))
