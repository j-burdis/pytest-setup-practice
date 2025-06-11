from unittest.mock import Mock
from lib.task_formatter import TaskFormatter

def test_mock_title_is_passed_to_formatter():
    task = Mock()
    task.title = "Walk the dog"
    formatter = TaskFormatter(task)
    assert formatter.task.title == "Walk the dog"

def test_mock_format_when_complete_false():
    task = Mock()
    task.title = "Walk the dog"
    task.complete = False
    formatter = TaskFormatter(task)
    assert formatter.format() == "- [ ] Walk the dog"

def test_mock_format_when_complete_true():
    task = Mock()
    task.title = "Walk the dog"
    task.complete = True
    formatter = TaskFormatter(task)
    assert formatter.format() == "- [x] Walk the dog"