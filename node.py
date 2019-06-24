# Árvore Rubro-Negra implementada em Python.

# The possible Node colors
BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'

class Node:
    def __init__(self, value, color, parent, left=None, right=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node with value: {self.value} and color {self.color}.'
