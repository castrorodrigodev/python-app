import os
from dotenv import load_dotenv
from utils import clear_console_3

load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

clear_console_3()
print(f"Hi {db_user}. Welcome to Python !!!")


print({
    "USER": db_user, 
    "PASSWORD": db_pass,
})
