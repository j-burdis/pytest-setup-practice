from lib.tasklist import TaskList
from lib.task import Task

def test_add_method_appends_one_task_to_tasklist():
    tasklist = TaskList()
    new_task = Task("Walk the dog")
    tasklist.add_task(new_task)
    assert tasklist.tasks == [new_task]

def test_add_method_appends_two_tasks_to_tasklist():
    tasklist = TaskList()
    new_task1 = Task("Walk the dog")
    new_task2= Task("Walk the cat")
    tasklist.add_task(new_task1)
    tasklist.add_task(new_task2)
    assert tasklist.tasks == [new_task1, new_task2]

def test_returns_list_of_incomplete_tasks():
    tasklist = TaskList()
    new_task1 = Task("Walk the dog")
    new_task2= Task("Walk the cat")
    tasklist.add_task(new_task1)
    tasklist.add_task(new_task2)
    assert tasklist.incomplete_tasks() == ["Walk the dog", "Walk the cat"]

def test_returns_list_of_incomplete_tasks_after_mark_complete():
    tasklist = TaskList()
    new_task1 = Task("Walk the dog")
    new_task2= Task("Walk the cat")
    tasklist.add_task(new_task1)
    tasklist.add_task(new_task2)
    new_task1.mark_complete()
    assert tasklist.incomplete_tasks() == ["Walk the cat"]

def test_returns_list_of_complete_tasks():
    tasklist = TaskList()
    new_task1 = Task("Walk the dog")
    new_task2= Task("Walk the cat")
    tasklist.add_task(new_task1)
    tasklist.add_task(new_task2)
    new_task1.mark_complete()
    assert tasklist.complete_tasks() == ["Walk the dog"]
    assert tasklist.incomplete_tasks() == ["Walk the cat"]

def test_returns_full_list_of_task_titles():
    tasklist = TaskList()
    new_task1 = Task("Walk the dog")
    new_task2= Task("Walk the cat")
    tasklist.add_task(new_task1)
    tasklist.add_task(new_task2)
    new_task1.mark_complete()
    assert tasklist.all_tasks() == ["Walk the dog", "Walk the cat"]