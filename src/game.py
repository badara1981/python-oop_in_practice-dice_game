from abc import ABC, abstractmethod
from dice import Dice


class Game(ABC):
    def __init__(self):
        self.gains = -10

    @abstractmethod
    def play_game(self):
        raise NotImplementedError()


class SumGame(Game):
    def play_game(self,gains):
        # Complete this method
        self.gains = gains
        gains = input("Play the Game and gains")
        return self.gains


class ParityGame(Game):
    def play_game(self, gains):
        # Complete this method
        self.gains = gains
        gains = input("ParityGame_ the winner")
        return self.gains

