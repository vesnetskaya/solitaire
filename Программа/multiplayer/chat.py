class Chat():
    def __init__(self):
        self.chat = []

    def send(self, message):
        self.chat.add(message)    