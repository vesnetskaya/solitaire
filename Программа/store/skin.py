class Skin():
    def __init__(self):
        self.skin = 'default'
        self.skins = []

    def change(self, num):
        self.skin = self.skins[num]