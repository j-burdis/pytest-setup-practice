class Diary:
    def __init__(self, contents):
        # contents is a string
        self._contents = contents

    def read(self):
        # Returns the contents of the diary
        return self._contents


# Integration tests
# Unit tests, exercising all of the class's functionality, 
# without using or referring to the other class.