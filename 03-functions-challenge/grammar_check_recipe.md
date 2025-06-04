# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE
def grammar_checker(text):
"""
    Extract first word and last word from a string
    Check first word starts uppercase
    Check last word has suitable punctuation at the end

    parameters: text, a string of words
    return: boolean, true if grammar is correct
    or 
    return: string, telling user to capitalise the start/add a 
            full stop to the end, or neither if grammar is good
    side effects: n/a
"""
```
## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Given an empty string
It returns an error
"""
grammar_checker("") => error

"""
Given a string of words with correct grammar
It returns a string with output "good job!"
"""
grammar_checker("A nice sentence.") => "Good job!"

"""
Given a string without a capital letter at the start
It returns a prompt to capitalise
"""
grammar_checker("a not so nice sentence.") => "Check your caps"

"""
Given a string without punctuation
It returns a prompt to add punctuation
"""
grammar_checker("A not so nice sentence") => "Check your punctuation"

"""
Given a string without a capital letter at the start or ending punctuation
It returns a prompt to check both capitalisation and punctuation
"""
grammar_checker("a not so nice sentence") => "Check your caps and punctuation"

"""
Given a None value
It throws an error
"""
grammar_checker(None) throws an error
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
It returns an error
"""
def test_empty_string_returns_error():
    with pytest.raises(Exception) as e:
        grammar_checker("")
    message = str(e.value)
    assert message == "Enter a string input"
```

Ensure all test function names are unique, otherwise pytest will ignore them!
