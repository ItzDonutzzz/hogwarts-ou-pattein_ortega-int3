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


def ask_number(message: str, min_val: int = None, max_val: int = None) -> int:
    """
    Demande un entier à l'utilisateur.
    - Supprime les espaces internes.
    - Gère le signe négatif (si le premier caractère est '-').
    - Applique les contraintes min_val / max_val si fournies.
    """
    while True:
        # Construire l'invite avec indication des bornes
        if min_val is not None and max_val is not None:
            hint = f"({min_val} - {max_val})"
        elif min_val is not None:
            hint = f"(minimum {min_val})"
        elif max_val is not None:
            hint = f"(maximum {max_val})"
        else:
            hint = ""
        prompt = f"{message} {hint}".strip() + ": "
        user_input = input(prompt).strip()

        # Enlever tous les espaces internes
        normalized = user_input.replace(" ", "")
        if not normalized:
            print("Entrée vide. Veuillez saisir un nombre entier.")
            continue

        # Vérifier le signe négatif (ou positif) et que le reste soit numérique
        if normalized[0] in "+-":
            rest = normalized[1:]
            sign = normalized[0]
        else:
            rest = normalized
            sign = ""
        if not rest.isdigit():
            print("Entrée invalide. Veuillez saisir un entier valide (ex: 42, -7).")

        # Conversion
        value = int(sign + rest)

        # Vérifications des bornes
        if min_val is not None and value < min_val:
            print(f"Veuillez saisir un nombre supérieur ou égal à {min_val}.")
        if max_val is not None and value > max_val:
            print(f"Veuillez saisir un nombre inférieur ou égal à {max_val}.")

        return value

def ask_choice(message, options):
    while True :
        print(message)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        user_input = input("Please select an option by entering the corresponding number: ").strip()

        choice = int(user_input)
        if choice not in (1, len(options)):
            return options[choice - 1]
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
