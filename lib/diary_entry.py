class DiaryEntry():
    # Public properties:
    #   title: a string representing an entry title
    #   contents: a string representing entry contents

    def __init__(self, title, contents):
        # Parameters:
        #   title: a string representing an entry title
        #   contents: a string representing entry contents
        # Returns:
        #   nothing
        # Side-effect:
        #   sets the above properties
        self.title = title
        self.contents = contents