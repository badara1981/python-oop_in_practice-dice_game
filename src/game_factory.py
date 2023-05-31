from game import ParityGame, SumGame


class GameFactory:
    @staticmethod
    def create_object(game_type):
        # Complete this method
        pass
        def __init__(self, parity, item):
         self.parity = parity
         self.item = item

    def get_position(self):
        return self.parity.coords(self.item)

    def move(self, x, y):
        self.parity.move(self.item, x, y)

    def delete(self):
        self.parity.delete(self.item)



def create_object(self, text):
    """Create an object given a text."""
    return self.get_queryset().get_or_create(
        **{self.create_field: text})[0]