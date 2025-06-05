class TaskManager():
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def all_tasks(self):
        if self._tasks:
            return self._tasks
        else:
            return "All tasks completed"

    def mark_complete(self, task):
        if task in self.all_tasks():
            self.all_tasks().remove(task)
        else:
            raise Exception("This task isn't in your list")