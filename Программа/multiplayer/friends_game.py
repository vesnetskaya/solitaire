class FriendsGame():
    def __init__(self):
        self.players = []

    def add(self, friend):
        self.players.add(friend)

    def delete(self, friend):
        self.players.delete(friend)