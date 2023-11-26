# raffle/utility.py

import os


def clear_console() -> None:
    match os.name:
        case "nt":
            os.system("cls")
        case other:
            os.system("clear")
