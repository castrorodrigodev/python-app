import os
from dotenv import load_dotenv
from utils.console import clear_console

load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_environment = os.getenv("ENV")

clear_console()

# result = {
#     "USER": f"Hi {db_user}. Welcome to Python !!!",
#     "PASS": db_pass,
#     "ENV": f"The environment is: {db_environment} !!!",
# }
# print(result)

# ************************ IF ************************
# age = int(input("Input  your age: "))
# if age < 18:
#     print("Not Adult person")
# else:
#     print("Adult person")

# ************************ IN - NOT IN ************************
# users = ["Rodrigo", "Fernando", "Giovani", "Damaris", "Emanuel"]
# print("Rodrigo" in users) # 1
# print("Rodrigo2" in users) # 2
# print("rodrigo" in users) # 3
# print("rod" in "Rodrigo") # 4
# print("Rod" in "Rodrigo") # 5
# print("sql" not in "SQL, Python, Java, TypeScript") # 6
# print("Sql" not in "Sql, Python, Java, TypeScript") # 7

# ************************ CONTINUE ************************
# my_name = "Rodrigo Castro"
# counter = 0
# for character in my_name:
#     if(character == " "):
#         continue
#     counter = counter + 1
# print(f"My fullname has {counter} characters")


# ************************ BREAK ************************
# email = input("Input your email please: ")
# for character in email:
#     if character == "@":
#         arroba = True
#         break
# else:
#     arroba = False

# print(arroba)


# ************************ GENERATORS ************************
def generateNumberGn(limit):
    num = 1
    while num < limit:
        yield num * 2
        num = num + 1


evenSeries = generateNumberGn(6)

# for i in evenSeries:
#     print(f"Element: {i}")

print(next(evenSeries))
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

returned_cities_2 = cities_gn_2("Berlin", "Roma", "Bogota", "Pekin", "Hanoi")  # Similar to cities_gn_3
print(next(returned_cities_2))  # B
print(next(returned_cities_2))  # e
print(next(returned_cities_2))  # r
# print(next(returned_cities))
# print(next(returned_cities))
