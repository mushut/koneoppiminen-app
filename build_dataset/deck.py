import card


class Deck:
    def __init__(self, id):
        self.id = id
        self.cards = []

        for suite_number in range(4):
            if suite_number == 0:
                suite = "diamond"
            elif suite_number == 1:
                suite = "heart"
            elif suite_number == 2:
                suite = "club"
            elif suite_number == 3:
                suite = "spade"

            for value in range(1,14):
                new_card = card.Card(suite, value)
                self.cards.append(new_card)


    # For printing the deck
    def to_string(self):
        result = ""
        for card in self.cards:
            result += card.to_string() + "\n"

        return result