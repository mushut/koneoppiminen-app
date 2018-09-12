class Deck:
    def __init__(self, id):
        self.id = id
        self.cards = ["1", "2", "3"]

    def to_string(self):
        return "".join(self.cards)