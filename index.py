import os
from dotenv import load_dotenv
from utils import clear_console_3

load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_environment = os.getenv("ENV")

clear_console_3()

result = {
    "USER": f"Hi {db_user}. Welcome to Python !!!",
    "PASS": db_pass,
    "ENV": f"The environment is: {db_environment} !!!",
}

print(result)
