from singleton_decorator import singleton
import random


@singleton
class Dice:
    def __init__(self):
        self.number_of_rolls = 0
        self.record = {}
        self.last_roll = 0
        for i in range(1, 7):
            self.record[str(i)] = 0, 0.00

    # complete this method
def roll(self):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    
    
    roll = []
    for _ in range(roll):
        roll = random.randint(1, 6)
        roll.append(roll)
        roll = -1
    return roll
    

def __str__(self):
        return str(self.record)

