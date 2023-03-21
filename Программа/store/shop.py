import currency
class Shop():
    def __init__(self):
        self.shop = []
        self.price = []
        self.currency = currency.Currency
    
    def buy(self):
        self.currency -= self.price