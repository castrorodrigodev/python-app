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
