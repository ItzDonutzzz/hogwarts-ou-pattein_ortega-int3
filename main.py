### game entry point, coordinates execution
from chapters.chapter_1 import introduction

if __name__ == "__main__":
    messages = [
        "Welcome to Chapter 1: The Beginning of Your Adventure!",
        "In this chapter, you will embark on a journey filled with challenges and discoveries.",
        "Welcome to the world of Harry Potter!",
    ]
    try:
        introduction(messages, delay=3)
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")

if __name__ == "__main__":
    last_name = input("Enter your character's last name: ")
    first_name = input("Enter your character's first name: ")
    print("Choose your character attributes:")
    courage = int(input("Courage level (1-10): "))
    intelligence = int(input("Intelligence level (1-10): "))
    loyalty = int(input("Loyalty level (1-10): "))
    ambition = int(input("Ambition level (1-10): "))

if __name__ == "__main __":
    print("Character profile:")
    print("Last Name:", last_name)
    print("First Name:", first_name)
    print("Money: 100")
    print("Inventory: ")
    print("Spells: ")
    print("Attributes:")
    print(" - Courage:", courage)
    print(" - Intelligence:", intelligence)
    print(" - Loyalty:", loyalty)
    print(" - Ambition:", ambition)
