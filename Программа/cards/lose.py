class Lose():
    def __init__(self):
        self.lose = False

    def lose(self):
        self.lose = True
    
    def restart(self):
        self.lose = False