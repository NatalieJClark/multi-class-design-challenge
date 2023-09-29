from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.readable_entry_extractor import ReadableEntryExtractor

"""
When I add a diary entry that fits in the time
And I call ReadableEntryExtractor#extract
With a wpm of 2 and a minutes of 2
It gets that diary entry
"""
def test_given_single_readable_entry_returns_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four")
    diary.add(entry_1)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == entry_1

"""
When I add one diary entry that does not fit in the time
And I call ReadableEntryExtractor#extract
With a wpm of 2 and a minutes of 2
It returns None
"""
def test_given_single_unreadable_entry_returns_none():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four five")
    diary.add(entry_1)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == None

"""
When I add mutiple diary entries, and one fits in the time
And I call ReadableEntryExtractor#extract
With a wpm of 2 and a minutes of 2
It returns the readable entry
"""
def test_given_readable_and_unreadable_returns_readable():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four five")
    entry_2 = DiaryEntry("My Title 1", "one two three four")
    diary.add(entry_1)
    diary.add(entry_2)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == entry_2

"""
When I add mutiple diary entries, including mutliple that fit in the time
And I call ReadableEntryExtractor#extract
With a wpm of 2 and a minutes of 2
It returns the longest readable entry
"""
def test_given_multiple_readable_returns_longest():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three four five")
    entry_2 = DiaryEntry("My Title 1", "one two three")
    entry_3 = DiaryEntry("My Title 1", "one two three four")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == entry_3

"""
When I add no diary entries
And I call ReadableEntryExtractor#extract
It returns None
"""
def test_given_no_entries_returns_none():
    diary = Diary()
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=2) == None
