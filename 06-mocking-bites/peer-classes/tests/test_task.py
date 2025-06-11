from lib.task import Task

def test_create_task_and_get_title():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"

def test_initially_task_is_not_complete():
    task = Task("Walk the dog")
    assert task.complete == False

def test_mark_complete_returns_true():
    task = Task("Walk the dog")
    assert task.complete == False
    task.mark_complete()
    assert task.complete == True
