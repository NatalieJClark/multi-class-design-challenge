from lib.task import Task

"""
Task constructs with a title
"""
def test_task_constructs_title():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"

"""
Task constructs as incomplete 
"""
def test_task_constructs_as_incomplete():
    task = Task("Walk the dog")
    assert task.complete == False

"""
When I mark task as complete
It is reflected in the complete property
"""
def test_marks_complete_complete_is_true():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.complete == True