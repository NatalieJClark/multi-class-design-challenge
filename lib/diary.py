from lib.diary_entry import DiaryEntry

class Diary():
    def __init__(self):
        self._entries = []
        
    def add(self, diary_entry):
        # Parameters:
        #   diary_entry: an instance of DiaryEntry
        # Returns:
        #   nothing
        # Side-effect:
        #   appends instance to a list of diary entries
        if not isinstance(diary_entry, DiaryEntry):
            raise Exception("Diary entry must be an instance of DiaryEntry class")
        self._entries.append(diary_entry)

    def all(self):
        # Returns:
        #   a list of DiaryEntry instances
        return self._entries