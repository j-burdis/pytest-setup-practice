import pytest
from lib.task_manager import TaskManager

def test_initialising_instance_creates_empty_list():
    manager = TaskManager()
    assert manager._tasks == []

def test_add_task_to_task_list():
    manager = TaskManager()
    manager.add_task("Walk the dog")
    assert manager._tasks == ["Walk the dog"]

def test_add_two_tasks_to_task_list():
    manager = TaskManager()
    manager.add_task("Walk the dog")
    manager.add_task("Wash the dishes")
    assert manager._tasks == ["Walk the dog", "Wash the dishes"]

def test_display_all_tasks():
    manager = TaskManager()
    manager.add_task("Walk the dog")
    manager.add_task("Wash the dishes")
    assert manager.all_tasks() == ["Walk the dog", "Wash the dishes"]

def test_display_message_when_task_list_empty():
    manager = TaskManager()
    assert manager.all_tasks() == "All tasks completed"

def test_mark_task_complete():
    manager = TaskManager()
    manager.add_task("Walk the dog")
    manager.add_task("Wash the dishes")
    manager.mark_complete("Walk the dog")
    assert manager.all_tasks() == ["Wash the dishes"]

def test_remove_task_not_in_list():
    manager = TaskManager()
    manager.add_task("Wash the dishes")
    with pytest.raises(Exception) as e:
        manager.mark_complete("Walk the dog")
    assert str(e.value) == "This task isn't in your list"
