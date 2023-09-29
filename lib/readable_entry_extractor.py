class ReadableEntryExtractor():
    def __init__(self, diary):
            # Parameters:
            #   diary: an instance of Diary
            # Returns:
            #   nothing
            # Side-effect: 
            #   set diary property
            self._diary = diary

    def extract(self, wpm, minutes):
        # Parameters:
        #   wpm: integer, representing reading speed
        #   minutes: an integer representing time
        # Returns:
        #   the longest diary entry that can be read
        #   given the wpm and minutes
        readable_entries = self._find_readable_entries(wpm, minutes)
        if len(readable_entries) == 0:
            return None
        else:
            return max(readable_entries, 
                key=lambda entry : self._count_words(entry.contents))
    
    def _find_readable_entries(self, wpm, minutes):
        return [entry for entry in self._diary.all()
            if self._is_entry_readable_in_time(wpm, minutes, entry)]
    
    def _is_entry_readable_in_time(self, wpm, minutes, entry):
        length_readable = wpm * minutes
        return self._count_words(entry.contents) <= length_readable
        
    def _count_words(self, string):
        return len(string.split())