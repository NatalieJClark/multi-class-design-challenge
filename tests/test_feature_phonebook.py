from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.phone_number_extractor import PhoneNumberExtractor
"""
When I add multiple diary entries
And I call PhoneNumberExtractor#extract
I get a set of phone numbers from all diary entry contents
"""
def test_extracts_phone_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 07800000001")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    entry_3 = DiaryEntry("My Title 3", "My friend is 07800000002")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07800000000", "07800000001", "07800000002"}

"""
When I add multiple diary entries
And I call PhoneNumberExtractor#extract
It ignores duplicate numbers
"""
def test_ignores_duplicate_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 07800000000")
    entry_2 = DiaryEntry("My Title 3", "My friend is 07800000000")
    diary.add(entry_1)
    diary.add(entry_2)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07800000000"}

"""
When I a diary entry
And I call PhoneNumberExtractor#extract
It ignores non-valid phone numbers
"""
def test_ignore_invalid_phone_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My friend is 078000000000 and45107800000000 and 0780, 13422")
    diary.add(entry_1)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == set()

"""
When I no diary entries
And I call PhoneNumberExtractor#extract
It returns None
"""
def test_given_no_entries_returns_empty():
    diary = Diary()
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == set()