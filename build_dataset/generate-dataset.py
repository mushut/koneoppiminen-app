# Generates deck dataset
import deck


def main():
    print("Deck generator")
    test = deck.Deck(1)
    print(test.to_string())


main()