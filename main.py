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
    character = init_character(
        {"last_name": last_name, "first_name": first_name},
        {
            "courage": courage,
            "intelligence": intelligence,
            "loyalty": loyalty,
            "ambition": ambition
        }
    )
    print("Character created successfully!")
    print(character)