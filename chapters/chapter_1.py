###introduction to chapter 1
import time

def introduction(messages, delay=1.0):
    for msg in messages:
        print(msg)
        time.sleep(delay)
    return(messages)

def create_character(last_name, first_name, courage, intelligence, loyalty, ambition):
    character = {
        "last_name": last_name,
        "first_name": first_name,
        "courage": courage,
        "intelligence": intelligence,
        "loyalty": loyalty,
        "ambition": ambition
    }
    return character

def init_character():


    character = create_character(last_name, first_name, courage, intelligence, loyalty, ambition)
    return character