from json import*
from random import*


def ask_text(message: str) -> str:
    user_input = input(message).strip()
    while not user_input:
        print("Input cannot be empty. Please enter valid text.")
        user_input = input(message).strip()
    return user_input
    """Demande à l'utilisateur de saisir du texte non vide."""


def ask_number(message: str, min_val: int = None, max_val: int = None):
    while True:
        user_input = input(message).strip()
        if user_input.startswith('-'):
            is_negative = True
            user_input = user_input[1:]
        else:
            is_negative = False

        if all(c.isdigit() for c in user_input) and user_input:
            number = 0
            for c in user_input:
                number = number * 10 + (ord(c) - ord('0'))
            if is_negative:
                number = -number

            if (min_val is None or number >= min_val) and (max_val is None or number <= max_val):
                return number
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        else:
            print("Invalid input. Please enter a valid integer.")
    """Demande à l'utilisateur de saisir un entier avec des limites optionnelles."""



