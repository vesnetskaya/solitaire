class Reports():
    def __init__(self):
        self.report = ''

    def send(self, report):
        self.report = report

    def ban(self, report):
        self.ban = True