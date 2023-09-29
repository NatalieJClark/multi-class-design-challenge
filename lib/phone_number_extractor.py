import re

class PhoneNumberExtractor():
    def __init__(self, diary):
        # Parameters:
        #   diary: an instance of Diary
        # Returns:
        #   nothing
        # Side-effect: 
        #   set diary property
        self._diary = diary

    def extract(self):
        # Returns:
        #   a list of phone numbers
        phone_numbers = set()
        for entry in self._diary.all():
            found_numbers = re.findall(r"\b0[0-9]{10}\b", entry.contents)
            phone_numbers.update(found_numbers)
        return phone_numbers