 # Red-black Tree implemented in Python 3.x

# The possible Node colors
BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'
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
			The Node's color. The Node will be always be initialized as having the color RED in the _insert function. AssertionError wil be raised if given
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
        """
        The purpose of this class is to be only used inside of our red-black tree, as it will be automatically instanciated inside it's functions as needed, 
        thus we assert that the node mnust have a parent. As a result of that choice, we won't be able to instanciate the class outside of the tree structure. 
        """
        # assert isinstance(parent, Node), "Parent must be a Node!"
        assert color == BLACK or color == RED, "Sorry, invalid color!"
        self.value  = value
        self.color  = color
        self.parent = parent
        self.left   = left
        self.right  = right

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
            return 'Node has value {self.value} and is {self.color}.\nHas no chidren and {self.parent} as parent node.'.format(self.value, self.color, self.color)
        elif self.left and not self.right:
            return 'Node has value {self.value} and is {self.color}.\nHas {self.left} as left child and {self.parent} as parent node.'.format(self.value, self.color, self.left, self.color)
        elif not self.left and self.right:
            return 'Node has value {self.value} and is {self.color}.\nHas {self.right} as right child and {self.parent} as parent node.'.format(self.value, self.color, self.right, self.color)
        else:
            return 'Node has value {self.value} and is {self.color}.\nHas two children, {self.left} and {self.right} as left and right child, respectively, and also {self.parent} as parent node.'.format(self.value, self.color, self.left, self.right, self.color)

