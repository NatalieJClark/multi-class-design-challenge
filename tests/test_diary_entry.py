from lib.diary_entry import DiaryEntry

"""
When a diary entry is constructed with a title and contents
We get the title and contents back as properties of the entry
"""
def test_diary_entry_constructs():
    entry = DiaryEntry("My Title", "My Contents")
    assert entry.title == "My Title"
    assert entry.contents == "My Contents"
