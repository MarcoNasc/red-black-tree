 # Red-black Tree implemented in Python 3.x

# The possible Node colors
BLACK = 'BLACK'
RED = 'RED'
colors = [BLACK, RED]


class Node:
    """
    Node of the red-black tree.
	Contains references to the sons (if any), the father and the color.
	"""
    def __init__(self, value, color, parent, left=None, right=None):
        """
        Class builder.

		Parameters
		----------
		self : Node
			A Node object.
		value : int
			The value assigned to the Node object. If not an integer, it will raise an AssertionError and give a message explaining the problem.
		color : str
			The Node color. The Node will be always be initialized as having the color RED in the insert() function. AssertionError wil be raised if given
        a color different from the two possible ones.
		parent : Node
			The parent Node. An AssertionError will be raised if an object of another type is provided.
        left: Node (default = None)
            The left child of the Node, also a Node object. 
        right: Node (default = None)
            The left child of the Node, also a Node object.
		-------
		Node
			A Node object.
		"""
        assert isinstance(value, int), "Value must be an integer!"    
        assert color in colors, "Sorry, invalid color!"
        self.value  = value
        self.color  = color
        self.parent = parent
        self.left   = left
        self.right  = right

    def __bool__(self):
        """
        Boolean verification.

		Used to verify the boolean value held by the Node object, this special method will be used to assign a False boolean value to the "NIL_LEAF", as it's value wil also be False.
        The goal of this implementation is to facilitate our verifications made in the beggining of every function inside the RedBlackTree().
		Parameters
		----------
		self : Node
			A Node object.
		Returns
		------
		bool
			The boolean value of the Node object, taking into account the aforementioned conditions.
		"""
        if self.value == False:
            return False
        return True

    def __repr__(self):
        """
        Character representation.

		Shows the value held by the Node object, as well as the previous one (the parent) and next ones (left and right children), if existent.
		Parameters
		----------
		self : Node
			A Node object.
		Returns
		-------
		str
			The representation of the Node object, containing the aforementioned characteristics.
		"""
        if not self.left and not self.right:
            return f'Node has value {self.value} and is {self.color}.\nHas no chidren and {self.parent.value} as parent node.'
        elif self.left and not self.right:
            return f'Node has value {self.value} and is {self.color}.\nHas {self.left.value} as left child and {self.parent.value} as parent node.'
        elif not self.left and self.right:
            return f'Node has value {self.value} and is {self.color}.\nHas {self.right.value} as right child and {self.parent.value} as parent node.'
        else:
            return f'Node has value {self.value} and is {self.color}.\nHas two children, {self.left.value} and {self.right.value} as left and right child, respectively, and also {self.parent.value} as parent node.'
        




        """
        # for python versions that don't accept fstrings, < v3.5
        if not self.left and not self.right:
            return 'Node has value {} and is {}.\nHas no chidren and {} as parent node.'.format(self.value, self.color, self.parent.value)
        elif self.left and not self.right:
            return 'Node has value {} and is {}.\nHas {} as left child and {} as parent node.'.format(self.value, self.color, self.left.value, self.parent.value)
        elif not self.left and self.right:
            return 'Node has value {} and is {}.\nHas {} as right child and {} as parent node.'.format(self.value, self.color, self.right.value, self.parent.value)
        else:
            return 'Node has value {} and is {}.\nHas two children, {} and {} as left and right child, respectively, and also {} as parent node.'.format(self.value, self.color, self.left.value, self.right.value, self.parent.value)
        """
