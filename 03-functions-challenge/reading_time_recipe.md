# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE
def reading_time_in_minutes(text):
    # parameters:
    # text, a string containing words
    # return:
    # integer, a number showing the number of minutes it will take to read the text
    # side effects: n/a
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an empty string
It returns zero
"""
reading_time_in_minutes("") => 0

"""
Given a string containing words
It returns an integer (to the nearest minute)
"""
reading_time_in_minutes("205 word string") => 1

"""
Given a None value
It throws an error
"""
reading_time_in_minutes(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given an empty string
It returns zero
"""
def reading_time_in_minutes(""):
    return 0
```

Ensure all test function names are unique, otherwise pytest will ignore them!
