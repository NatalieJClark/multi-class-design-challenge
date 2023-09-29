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
        self._entries.append(diary_entry)

    def all(self):
        # Returns:
        #   a list of DiaryEntry instances
        return self._entries