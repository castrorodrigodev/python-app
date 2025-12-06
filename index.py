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

# age = int(input("Input  your age: "))

# if age < 18:
#     print("Not Adult person")
# else:
#     print("Adult person")

# users = ["Rodrigo", "Fernando", "Giovani", "Damaris", "Emanuel"]
# print("Rodrigo" in users) # 1
# print("Rodrigo2" in users) # 2
# print("rodrigo" in users) # 3
# print("rod" in "Rodrigo") # 4
# print("Rod" in "Rodrigo") # 5
# print("sql" not in "SQL, Python, Java, TypeScript") # 6
# print("Sql" not in "Sql, Python, Java, TypeScript") # 7

# my_name = "Rodrigo Castro"
# counter = 0
# for character in my_name:
#     if(character == " "):
#         continue
#     counter = counter + 1
# print(f"My fullname has {counter} characters")


# email = input("Input your email please: ")
# for character in email:
#     if character == "@":
#         arroba = True
#         break
# else:
#     arroba = False

# print(arroba)
