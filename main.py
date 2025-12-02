### game entry point, coordinates execution
for i in range(5):
    print(f"Game loop iteration {i+1}")
    # Here would be the main game logic
import random

def roll_dice(sides=6):
    return random.randint(1, sides)