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

def init_character(tuple):
    attributes = {
        "Character profile": "",
        "last_name": tuple[0],
        "first_name": tuple[1],
        "Money : 100": "",
        "Inventory :": "",
        "Spells :": "",
        "Attributes :": "",
        "courage": tuple[2],
        "intelligence": tuple[3],
        "loyalty": tuple[4],
        "ambition": tuple[5]
    }
    return attributes


