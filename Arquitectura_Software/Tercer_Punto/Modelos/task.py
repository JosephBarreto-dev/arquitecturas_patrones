class TaskStore:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def add(self, title):
        self.tasks.append({"id": self.counter, "title": title, "done": False})
        self.counter += 1

    def get_all(self):
        return self.tasks

    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
