import pytest
from lib.todo import Todo

def test_creating_a_todo_sets_complete_to_False():
    task = Todo("Walk the dog")
    assert task._complete == False

def test_create_todo_and_get_contents():
    task = Todo("Walk the dog")
    assert task._task == "Walk the dog"

def test_mark_complete_sets_to_true():
    task = Todo("Walk the dog")
    task.mark_complete()
    assert task._complete == True

def test_mark_complete_on_completed_todo_returns_error_message():
    todo = Todo("Walk the dog")
    todo.mark_complete()
    with pytest.raises(Exception) as e:
        todo.mark_complete()
    message = str(e.value)
    assert message == "You've already marked this complete!"
