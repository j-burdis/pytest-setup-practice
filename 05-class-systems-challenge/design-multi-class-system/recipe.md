# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

┌───────────────────────────────┐     ┌───────────────────────────┐  
│ Diary                         │     │ TaskList                  │  
│                               │     │                           │  
│ - add(entry)                  │     │ - add_task(task)          │  
│                               │     │                           │  
│ - all_entries()               │     │ - mark_complete()         │  
│                               │     │                           │  
│ - entry_for_time_wpm(time,wpm)│     │ - incomplete_tasks        │  
│                               │     │                           │  
│ - find_mobile_numbers()       │     │ - complete_tasks          │  
└───────────────────────────────┘     └───────────────────────────┘  

┌───────────────────────────┐         ┌───────────────────────────┐  
│ DiaryEntry                │         │ Task                      │  
│                           │         │                           │  
│ - init(title, contents)   │         │ - init(title)             │  
│                           │         │                           │  
│ - word_count              │         │ - complete()              │  
└───────────────────────────┘         └───────────────────────────┘  


```python
# EXAMPLE

class Diary:
    def __init__(self):
        # Side effects:
        #   Creates empty list
        # self.diary = []
        pass # No code here yet

    def add(self, entry):
        # Params:
        #    diary entry instance variable
        # Side effects:
        #   appends entry to the diary list
        # self.diary.append(entry)
        pass

    def all_entries(self):
        # Returns:
        #   list of all entries in the diary
        # return self.diary
        pass

    def entry_for_time_wpm(self, time, wpm):
        # Params:
        #   integers: time available and user's words per minute
        # Returns:
        #   the diary entry that most closely fits the reading time
        #   available based on the user's wpm
        #  or titles of all entries that the user can read in the
        #  time available? in ascending order? or with reading time shown?
        pass

    def find_mobile_numbers(self)
        # Returns:
        #   list of all the mobile numbers in all diary entries
        pass


class DiaryEntry:
    def __init__(self, title, contents)
        # Parameters:
        #   string: for both title and contents for the diary entry
        # Returns:
        #   Nothing
        # Side effects:
        #   Saves the entry to the self object
        # self.title = title
        # self.contents = contents
        pass

    def word_count(self):
        # Returns:
        #   word count of the contents of the diary entry
        # return len(self.contents.split())
        pass


class TaskList:
    def __init__(self):
        # Side effects:
        #   creates empty task list
        # self.task_list = []
        pass

    def add(self, task):
        # Params:
        #   instance variable of the task to be added
        # Side effects:
        #   appends task to the task list containing all tasks
        # self.task_list.append(task)
        pass

    def mark_complete(self):
        # Side effects:
        #   sets the value of the complete property to True
        # task.complete = True
        pass

    def incomplete_tasks(self):
        # Returns: 
        #   a list of incomplete tasks
        # return [task for task in task_list if not task.complete]
        pass

    def complete_tasks(self):
        # Returns: 
        #   a list of complete tasks
        # return [task for task in task_list if task.complete]
        pass

class Task:
    def __init__(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side effects
        #   Saves the task to the self object
        #   Sets the complete property to false
        # self.task = task
        # self.complete = False
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
