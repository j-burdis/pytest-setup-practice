# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskManager:
    # User-facing properties:
    #   name: string

    def __init__(self, tasks):
        # Parameters:
        #   tasks: list, to store the tasks somewhere
        # Side effects:
        #   Sets the tasks property of the self object
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side effects:
        #   Saves the task to the self object (the list of tasks)
        pass # No code here yet

    def all_tasks(self)
        # Parameters: 
        #   None 
        # Returns:
        #   The list of all the tasks to complete
        # Side effects: 
        #   None
        pass

    def mark_complete(self, task)
        # Parameters: 
        #   string, the task to mark to complete
        # Returns:
        #   Nothing 
        # Side effects:
        #   Removes task from list
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task to add
#add_task appends it to the task list
"""
task_manager = TaskManager()
task_manager.add_task("Walk the dog")

"""
When the user needs to see their task list
#all_tasks displays their incomplete tasks
"""
task_manager = TaskManager()
task_manager.all_tasks() # display list of outstanding tasks => ["Walk the dog"]

"""
Given a name of a task in the list
#mark_complete removes this task from the list or throws and error if it isn't present
"""
task_manager = TaskManager()
task_manager.mark_complete("Walk the dog")
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
