from lib.tasklist import TaskList

def test_initially_tasklist_is_an_empty_list():
    tasklist = TaskList()
    assert tasklist.tasks == []

def test_returns_empty_list_of_incomplete_tasks():
    tasklist = TaskList()
    assert tasklist.incomplete_tasks() == []