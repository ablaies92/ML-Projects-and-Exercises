"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""
# __init__ is called a class constructor
# def() is called a method for the class XXXX

class Stack:
    # the function below includes an constructor "__init__"
    # we are going to create an object "stack" that is of the class Stack (creating an object from the template)
    def __init__(self):
        # items property/attribute
        self.items = []
    # checking to see if a list is empty
    def is_empty(self):
        # return len(self.items) == 0
        # an empty list evaluates as false, so the bottom statement is the most pythonic way to check and
        # see if a list is empty
        return not self.items
    # push method/function
    def push(self, item):
        self.items.append(item)
    def pop(self):
        # returns the far right value and removes it
        return self.items.pop()
    def peek(self):
        # accessing the end of the list
        return self.items[-1]
    def size(self):
        return len(self.items)
    # let's us use the print statement to inspect our stack
    def __str__(self):
        return str(self.items)
    # if you don't include pass, you'll return an error
    #pass

# if we want to import something into a file, the below code allows us to do so
# essentially checking to see if the current file we are running is the main file (from the command line)
# if not, just use the class and don't worry about the code below
# essentially, the current .py file that you are running is considered to be __main__
# to call on the Stack() class module in another file, one would have to use "import stack"
if __name__ == "__main__":
    # s is an instance of the class Stack; calls on the constructor
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())