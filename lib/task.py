class Task():
    # Public properties:
    #   title: a string representing a job to do
    #   complete: a boolean representing whether it is complete

    def __init__(self, title):
        # Parameters:
        #   title: a string representing a job to do
        #   complete: a boolean, initially False
        # Returns:
        #   nothing
        # Side-effect:
        #   sets the above properties   
        self.title = title
        self.complete = False

    def mark_complete(self):
        # Side-effect:
        #   mark the task complete
        # Returns:
        #   nothing
        self.complete = True