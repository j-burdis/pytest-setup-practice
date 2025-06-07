from lib.todo_list import TodoList

def test_initally_incomplete_todos_is_empty():
    todo_list = TodoList()
    assert todo_list._incomplete_todos == []

def test_initally_complete_todos_is_empty():
    todo_list = TodoList()
    assert todo_list._complete_todos == []

def test_incomplete_method_returns_empty_list():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

def test_complete_method_returns_empty_list():
    todo_list = TodoList()
    assert todo_list.complete() == []