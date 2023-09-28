# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
>>> Add tasks, mark complete, list complete, list incomplete

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
>>> A phone number starts with zero and is eleven digits long

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. 
Extracting the verbs and nouns from the user story, is a simple but powerful technique to help you plan the classes and their methods. 
Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
Nouns:
diary
diary entry
experiences
time
reading speed
task
todo list
phone number
list of phone numbers

Verbs:
record
keep
reflect
read
select
keep
see a list
mark complete
list complete
list incomplete
add

_Also design the interface of each class in more detail._

```python

class Diary():
    def add(self, diary_entry):
        # Parameters:
        #   diary_entry: an instance of DiaryEntry
        # Returns:
        #   nothing
        # Side-effect:
        #   appends instance to a list of diary entries
        pass

    def all(self):
        # Returns:
        #   a list of DiaryEntry instances
        pass

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
        pass

class TaskList():
    def add(self, task):
        # Parameters:
        #   task: an intance of Task
        # Returns:
        #   nothing
        # Side-effect:
        #   adds instance to list of tasks
        pass

    def all_incomplete(self):
        # Returns:
        #   a filtered list of instances of Task, representing the incomplete tasks
        pass
   
    def all_complete(self):
        # Returns:
        #   a filtered list of instances of Task, representing the complete tasks
        pass

class Task():
    # Public properties:
    #   title: a string representing a job to do
    #   complete?

    def __init__(self, title, complete):
        # Parameters:
        #   title: a string representing a job to do
        #   ?complete: a boolean, True if complete, False otherwise (initially False)
        # Returns:
        #   nothing
        # Side-effect:
        #   sets the above properties   
        pass

    def mark_complete(self):
        # Side-effect:
        #   mark the task complete
        # Returns:
        #   nothing
        pass

class PhoneNumberExtractor():
    def __init__(self, diary):
        # Parameters:
        #   diary: an instance of Diary
        # Returns:
        #   nothing
        # Side-effect: 
        #   set diary property
        pass

    def extract(self):
        # Returns:
        #   a list of phone numbers
        pass

class ReadableEntryExtractor():
def __init__(self, diary):
        # Parameters:
        #   diary: an instance of Diary
        # Returns:
        #   nothing
        # Side-effect: 
        #   set diary property
        pass

    def extract(self, wpm, minutes):
        # Parameters:
        #   wpm: integer, representing reading speed
        #   minutes: an integer representing time
        # Returns:
        #   the longest diary entry that can be read
        #   given the wpm and minutes
        pass


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

"""
When I add multiple diary entries
#all lists them out in the order they were added 
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My Contents 1")
entry_2 = DiaryEntry("My Title 2", "My Contents 2")
entry_3 = DiaryEntry("My Title 3", "My Contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.all() #=> [entry_1, entry_2, entry_3]

"""
When I add multiple task instances
And I don't mark any complete
#all_incomplete lists them out in the order they were added
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_list.all_incomplete() #=> [task_1, task_2, task_3]

"""
When I add multiple task instances
And I mark one complete
#all_incomplete lists only the incomplete task
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_complete() #=> [task_2]

"""
When I add multiple task instances
And I mark one complete
#all_complete lists the complete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_incomplete() #=> [task_1, task_3]

"""
When I add multiple diary entries
And I call PhoneNumberExtractor#extract
I get a list of phone numbers from all diary entry contents
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 07800000001")
entry_2 = DiaryEntry("My Title 2", "My Contents 2")
entry_3 = DiaryEntry("My Title 3", "My friend is 07800000002")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = PhoneNumberExtractor(diary)
extractor.extract() #=> ["07800000000", "07800000001", "07800000002"]

"""
When I add multiple diary entries
And I call PhoneNumberExtractor#extract
It ignores duplicate numbers"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 07800000000 and 07800000000")
entry_2 = DiaryEntry("My Title 3", "My friend is 07800000000")
diary.add(entry_1)
diary.add(entry_2)
extractor = PhoneNumberExtractor(diary)
extractor.extract() #=> ["07800000000"]

"""
When I a diary entry
And I call PhoneNumberExtractor#extract
It ignores non-valid phone numbers
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "My friend is 078000000000 and 0780000 and 0780, 13422")
diary.add(entry_1)
extractor = PhoneNumberExtractor(diary)
extractor.extract() #=> []

"""
When I no diary entries
And I call PhoneNumberExtractor#extract
It returns None
"""
diary = Diary()
extractor = PhoneNumberExtractor(diary)
extractor.extract() #=> None

"""
When I add a diary entry that fits in the time
And I call ReadableEntryExtractor#extract
With a wpm of 2 and a minutes of 2
It gets that diary entry
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four")
diary.add(entry_1)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) #=> entry_1

"""
When I add one diary entry that does not fit in the time
And I call ReadableEntryExtractor#extract
With a wpm of 2 and a minutes of 2
It returns None
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four five")
diary.add(entry_1)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) #=> None

"""
When I add mutiple diary entries, and one fits in the time
And I call ReadableEntryExtractor#extract
With a wpm of 2 and a minutes of 2
It returns the readable entry
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four five")
entry_2 = DiaryEntry("My Title 1", "one two three four")
diary.add(entry_1)
diary.add(entry_2)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) #=> entry_2

"""
When I add mutiple diary entries, including mutliple that fit in the time
And I call ReadableEntryExtractor#extract
With a wpm of 2 and a minutes of 2
It returns the longest readable entry
"""
diary = Diary()
entry_1 = DiaryEntry("My Title 1", "one two three four five")
entry_2 = DiaryEntry("My Title 1", "one two three four")
entry_2 = DiaryEntry("My Title 1", "one two three")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) #=> entry_2

"""
When I add no diary entries
And I call ReadableEntryExtractor#extract
It returns None
"""
diary = Diary()
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) #=> None

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

# Diary
"""
Initially, Diary has no entries
"""
diary = Diary()
diary.all() #=> []


# DiaryEntry
"""
When a diary entry is constructed with a title and contents
We get the title and contents back as properties of the entry
"""
entry_1 = DiaryEntry("My Title", "My Contents")
entry.title #=> "My Title"
entry.contents #=> "My Contents"

# TaskList
"""
Initially, TaskList has no incomplete tasks
"""
task_list = TaskList()
task_list.all_incomplete() #=> []

"""
Initially, TaskList has no complete tasks
"""
task_list = TaskList()
task_list.all_complete() #=> []

# Task
"""
Task constructs with a title
"""
task = Task("Walk the dog")
task.title #=> "Walk the dog"

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
