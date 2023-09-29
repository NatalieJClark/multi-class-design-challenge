from lib.task_list import TaskList

"""
Initially, TaskList has no incomplete tasks
"""
def test_initially_no_incomplete():
    task_list = TaskList()
    assert task_list.all_incomplete() == []

"""
Initially, TaskList has no complete tasks
"""
def test_initially_no_complete():
    task_list = TaskList()
    assert task_list.all_complete() == []