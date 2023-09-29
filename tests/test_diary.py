from lib.diary import Diary
import pytest

"""
Initially, Diary has no entries
"""
def test_diary_constructs_with_no_entries():
    diary = Diary()
    assert diary.all() == []