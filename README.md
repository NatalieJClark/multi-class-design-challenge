# Multi Class Organiser

## Introduction
- This is my repo for Makers Module 2 - Golden Square: Designing a Multi Class System
- This project was a challenge for this module section
- The `organiser_design_recipe.md` documents my design of the class system and tests based on the given user stories
- This project is a multi-class system, containing DiaryEntry, Diary, Task, TaskList, PhoneNumberExtractor and ReadableEntryExtractor classes
- It used TDD and so contains unit and integration tests
- It satisfies all the user stories in the objectives below

<img width="1153" alt="image" src="https://github.com/NatalieJClark/multi-class-organiser/assets/107806810/86cae84d-9d6f-4aea-9daf-2f7f4ccb640d">

  
## Objectives
Complete the following challenge:

- [x] Use object-oriented design and test-driven development, backed up by your debugging and pairing skills, to develop the following program
  - [x] As a user  
        So that I can record my experiences  
        I want to keep a regular diary
  - [x] As a user  
        So that I can reflect on my experiences  
        I want to read my past diary entries
  - [x] As a user  
        So that I can reflect on my experiences in my busy day  
        I want to select diary entries to read based on how much time I have and my reading speed
  - [x] As a user  
        So that I can keep track of my tasks  
        I want to keep a todo list along with my diary
  - [x] As a user  
        So that I can keep track of my contacts  
        I want to see a list of all of the mobile phone numbers in all my diary entries  

Remember that user stories don't map to classes 1:1. You'll need to digest the full problem and then develop a multi-class system that meets the user's needs.
Don't worry about user interface or input-output. That means you shouldn't be using input() and only use print() for debugging purposes.

## Setup
This project uses `python`, `pyenv` and `pipenv`. Here's how to install it:

```shell
# Install pyenv, a tool to manage different versions of Python.
# This will ensure you have the latest Python, which has more readable error messages.
; brew install pyenv
# You may be given some extra instructions at the end of the command.
# If you are, follow them. If not, keep going.

# Now install the latest Python.
; pyenv install 3.11

# Install pipenv
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version # Check pipenv is installed
pipenv, version ...
```
To test the practise code: 
```shell
# Install the dependencies (pytest)
; pipenv install # NB: you may need to change interpreters to import pytest

# Optionally ...
# Activate the project's virtualenv
; pipenv shell

# If using the pipenv shell:
# This runs all of the tests in the current directory
; pytest
# And this exits the pipenv shell
; exit # or Ctrl-D

# Otherwise, this runs all of the tests in the current directory
; pipenv run pytest
```
