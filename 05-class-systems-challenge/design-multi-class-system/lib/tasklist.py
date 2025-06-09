class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def incomplete_tasks(self):
        return [task.title for task in self.tasks if task.complete == False]

    def complete_tasks(self):
        return [task.title for task in self.tasks if task.complete == True]

    def all_tasks(self):
        return [task.title for task in self.tasks]
