class Tasks():
    def __init__(self):
        self.tasks = []
        self.done_tasks = []

    def done(self, task):
        self.tasks.remove(task)
        self.done_tasks.add(task)