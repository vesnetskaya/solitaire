class Deal():
    def __init__(self):
        self.cards = []

    def deal(self, new_cards):
        self.cards = new_cards

    def back(self):
        self.cards = []