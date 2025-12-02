import numbers
from json import*
from random import*


def ask_text(message: str):
    user_input = input(message).strip()
    while not user_input:
        print("Input cannot be empty. Please enter valid text.")
        user_input = input(message).strip()
    return user_input
    """Demande à l'utilisateur de saisir du texte non vide."""


def ask_number(message: str, min_val=None, max_val=None):
while True:
    if min_val is not None and max_val is not None:
        user_input = input(message , f"({min_val} - {max_val})").strip()
        try:
            value = int(user_input)
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                if min_val is not None and max_val is not None:
                    print(f"Please enter a number between {min_val} and {max_val}.")
                elif min_val is not None:
                    print(f"Please enter a number greater than or equal to {min_val}.")
                elif max_val is not None:
                    print(f"Please enter a number less than or equal to {max_val}.")
            else:
                return value

    elif min_val is not None and max_val is None:
        user_input = input(message , f"(minimum {min_val})").strip()
        try:
            value = int(user_input)
            if value < min_val:
                print(f"Please enter a number greater than or equal to {min_val}.")
            else:
                return value

    elif max_val is not None and min_val is None:
        user_input = input(message , f"(maximum {max_val})").strip()
        try:
            value = int(user_input)
            if value > max_val:
                print(f"Please enter a number less than or equal to {max_val}.")
            else:
                return value

    else:
        user_input = input(message).strip()
        try:
            value = int(user_input)
            return value


    except ValueError:
        print("Invalid input. Please enter a valid integer.")





