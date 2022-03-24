"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""
import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# solution from instructor
# adding each character from the string to the s variable which is calling on class Stack
for char in string:
    s.push(char)
print(s)

while not s.is_empty():
    reversed_string += s.pop()
print(reversed_string)