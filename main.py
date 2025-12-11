### game entry point, coordinates execution

from utils.input_utils import *
from chapters.chapter_1 import *
if __name__ == "__main__":
    messages = [
        "Welcome to Chapter 1: The Beginning of Your Adventure!",
        "In this chapter, you will embark on a journey filled with challenges and discoveries.",
        "Welcome to the world of Harry Potter!",
    ]
    introduction(messages, delay=3)


    last_name = ask_text("Enter your character's last name: ")
    first_name = ask_text("Enter your character's first name: ")
    print("Choose your character attributes:")
    courage = ask_number("Courage level (1-10): ")
    intelligence = ask_number("Intelligence level (1-10): ")
    loyalty = ask_number("Loyalty level (1-10): ")
    ambition = ask_number("Ambition level (1-10): ")
    attributes = {last_name, first_name, courage, intelligence, loyalty, ambition}


