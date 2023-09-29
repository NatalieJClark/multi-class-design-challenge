from lib.diary import Diary
import pytest

"""
Initially, Diary has no entries
"""
def test_diary_constructs_with_no_entries():
    diary = Diary()
    assert diary.all() == []

"""
Given diary_entry that is not an instance of DiaryEntry class
#add Raises an error
"""
def test_todo_not_instance_of_todo_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.add("diary_entry")
    assert str(e.value) == "Diary entry must be an instance of DiaryEntry class"