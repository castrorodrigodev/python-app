import os
import platform


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def clear_console_2():
    is_windows = platform.system() == "Windows"
    os.system("cls" if is_windows else "clear")


def clear_console_3():
    cmds = {
        "Windows": "cls",
        "Linux": "clear",
        "Darwin": "clear",
    }
    os.system(cmds.get(platform.system(), "clear"))
