class TaskList():
    def __init__(self):
        self._tasks = []

    def add(self, task):
        # Parameters:
        #   task: an intance of Task
        # Returns:
        #   nothing
        # Side-effect:
        #   adds instance to list of tasks
        self._tasks.append(task)

    def all_incomplete(self):
        # Returns:
        #   a filtered list of instances of Task, representing the incomplete tasks
        return [
            task for task in self._tasks 
            if not task.complete
        ]
   
    def all_complete(self):
        # Returns:
        #   a filtered list of instances of Task, representing the complete tasks
        return [
            task for task in self._tasks
            if task.complete
        ]