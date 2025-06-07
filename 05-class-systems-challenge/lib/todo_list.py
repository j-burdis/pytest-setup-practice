class TodoList:
    def __init__(self):
        self._incomplete_todos = []
        self._complete_todos = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        if todo._task in self.incomplete():
            raise Exception("This is already in your todo list!")
        self._incomplete_todos.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        for todo in self._incomplete_todos:
            if todo._complete == True:
                self._complete_todos.append(todo)
                self._incomplete_todos.remove(todo)
        return [todo._task for todo in self._incomplete_todos]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [todo._task for todo in self._complete_todos]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self._incomplete_todos:
            todo.mark_complete()
        self.incomplete()
