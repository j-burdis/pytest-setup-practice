from lib.task import Task

def test_task_created_as_string_with_complete_as_false():
    new_task = Task("Walk the dog")
    assert new_task.title == "Walk the dog"
    assert new_task.complete == False

def test_mark_complete_returns_true():
    new_task = Task("Walk the dog")
    new_task.mark_complete()
    assert new_task.complete == True