class Currency():
    def __init__(self):
        self.currency = 500
    
    def add(self, money):
        self.currency += money

    def sub(self, money):
        self.currency -= money
        