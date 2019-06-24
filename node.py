# Red-black Tree implemented in Python 3.x

# The possible Node colors
BLACK = 'BLACK'
RED = 'RED'

# The node class that will be used in our tree structure.
# It has no children as default and takes value, color and parent node as parameters.
# In the insert function, is always initialized with RED color.
class Node:
    def __init__(self, value, color, parent, left=None, right=None):
        self.value  = value
        self.color  = color
        self.parent = parent
        self.left   = left
        self.right  = right

    def __repr__(self):
        return f'Node has value {self.value} and is {self.color}.'
