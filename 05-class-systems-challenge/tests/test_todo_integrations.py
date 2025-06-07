import pytest
from lib.todo import Todo
from lib.todo_list import TodoList

def test_add_method_adds_todo_to_incomplete_todos():
    todo_list = TodoList()
    todo = Todo("Walk the dog")
    todo_list.add(todo)
    assert todo_list.incomplete() == ["Walk the dog"]

def test_add_method_adds_multiple_todos_to_incomplete_todos():
    todo_list = TodoList()
    todo1 = Todo("Walk the dog")
    todo2 = Todo("Wash the car")
    todo3 = Todo("Do the dishes")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    assert todo_list.incomplete() == ["Walk the dog", "Wash the car", "Do the dishes"]

def test_mark_complete_moves_todo_from_incomplete_todos_to_complete_todos():
    todo_list = TodoList()
    todo1 = Todo("Walk the dog")
    todo_list.add(todo1)
    assert todo_list.incomplete() == ["Walk the dog"]
    todo1.mark_complete()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == ["Walk the dog"]

def test_mark_complete_moves_multiple_todos_from_incomplete_todos_to_complete_todos():
    todo_list = TodoList()
    todo1 = Todo("Walk the dog")
    todo2 = Todo("Clean the house")
    todo3 = Todo("Do the dishes")
    todo4 = Todo("Wash the car")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo_list.add(todo4)
    assert todo_list.incomplete() == ["Walk the dog", "Clean the house", "Do the dishes", "Wash the car"]
    todo1.mark_complete()
    todo4.mark_complete()
    assert todo_list.incomplete() == ["Clean the house", "Do the dishes"]
    assert todo_list.complete() == ["Walk the dog", "Wash the car"]

def test_give_up_method_moves_all_todos_to_complete():
    todo_list = TodoList()
    todo1 = Todo("Walk the dog")
    todo2 = Todo("Clean the house")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.incomplete() == ["Walk the dog", "Clean the house"]
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == ["Walk the dog", "Clean the house"]

def test_adding_same_todo_twice_returns_error_message():
    todo_list = TodoList()
    todo1 = Todo("Walk the dog")
    todo2 = Todo("Walk the dog")
    todo_list.add(todo1)
    with pytest.raises(Exception) as e:
        todo_list.add(todo2)
    message = str(e.value)
    assert message == "This is already in your todo list!"
