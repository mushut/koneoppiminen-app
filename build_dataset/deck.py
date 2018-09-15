import card
import random


class Deck:
    def __init__(self, id):
        self.id = id
        self.cards = []
        cards = []

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
                cards.append(new_card)

        rand_indexes = []
        number = 0
        for i in range(52):
            rand_indexes.append(number)
            number += 1

        for index in range(52):
            rand_index = random.randint(0,len(rand_indexes)-1)
            rand_indexes.remove(rand_indexes[rand_index])
            self.cards.append(cards[rand_index])


    # For printing the deck
    def to_string(self):
        result = ""
        for card in self.cards:
            result += card.to_string() + "\n"

        return result