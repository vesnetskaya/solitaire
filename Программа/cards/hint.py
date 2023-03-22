class Hint():
    def __init__(self):
        self.hint = False

    def recharge(self):
        self.hint = True

    def use(self):
        self.hint = False