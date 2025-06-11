from lib.task import Task
from lib.task_formatter import TaskFormatter

def test_task_title_is_passed_to_formatter():
    task = Task("Walk the dog")
    formatter = TaskFormatter(task)
    assert formatter.task.title == "Walk the dog"

def test_format_method_returns_empty_box_when_incomplete():
    task = Task("Walk the dog")
    formatter = TaskFormatter(task)
    assert formatter.format() == "- [ ] Walk the dog"

def test_format_method_returns_x_when_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    formatter = TaskFormatter(task)
    assert formatter.format() == "- [x] Walk the dog"
