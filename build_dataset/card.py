class Card:
    def __init__(self, new_suite, new_value):
        self.suite = new_suite
        self.value = new_value

    def to_string(self):
        return self.suite + " - " + str(self.value)