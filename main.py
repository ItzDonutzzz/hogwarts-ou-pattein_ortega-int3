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


    create_character(ask_text("Enter your character's last name: "),
                     ask_text("Enter your character's first name: "),
                     ask_number("Courage level ",1,10),
                     ask_number("Intelligence level ",1,10),
                     ask_number("Loyalty level ",1,10),
                     ask_number("Ambition level ",1,10))
    attributes =
    init_character(attributes)


