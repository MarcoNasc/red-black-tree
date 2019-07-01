# Red-black Tree implemented in Python 3.x

from node import *

# Usual functions are used to check if there is a root in the tree
# and to call their pair "private" _function. Those two parts could be brought together,
# but are divided for organization purposes.
    
class RedBlackTree:
    
    # class DuplicateValueError(Exception):
    #     '''Raise when a certain value is to be inserted, but is already in tree.'''
    #     pass
    # class ValueError(Exception):
    #     '''Raise when any operation other than insertion is attempted, if the tree is empty'''
    #     pass
    NIL_LEAF = Node(value=False, color=BLACK, parent=None)

    def __init__(self):
        """
        Class builder.

		Parameters
		----------
		self : RedBlackTree
			A RedBlackTree object.
            The tree is initialized empty at first, without a root. The first call to the insert() function will set the root of the tree.
        ------
        root : Node (default = None)
            The tree is initialized empty at first, without a root. The first call to the insert() function will set the root of the tree.
        ------
		RedBlackTree
			A RedBlackTree object.
		"""
        self.root = self.NIL_LEAF

    def __repr__(self):
        if self.root == self.NIL_LEAF:
            return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.height(self.root)  # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0:
                break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.value:
                    buf = ' ' * int((5 - len(str(n.value))) / 2)
                    if n.color == RED:
                        # cur_row += f"{buf}{RED, str(n.value)}{buf}" + sep
                        cur_row += '%s%s%s'%(buf, RED+str(n.value),buf)+sep
                    elif n.color == BLACK:
                        # cur_row += f"{buf}{BLACK, str(n.value)}{buf}" + sep
                        cur_row+='%s%s%s'%(buf, BLACK+str(n.value),buf)+sep

                else:
                    cur_row += ' ' * 5 + sep

                if n.left:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    def insert(self, value):
        if self.root == self.NIL_LEAF:
            self.root = Node(value, color=BLACK, parent=self.NIL_LEAF, left=self.NIL_LEAF, right=self.NIL_LEAF)
        else:
            self._insert(value, self.root)

    def _insert(self, value, parent_node):
        if value < parent_node.value:
            if not parent_node.left:
                parent_node.left = Node(value, color=RED, parent=parent_node, left=self.NIL_LEAF, right=self.NIL_LEAF)
                self._rebalance_node(parent_node.left)
            else:
                self._insert(value, parent_node.left)

        elif value > parent_node.value:
            if not parent_node.right:
                parent_node.right = Node(value, color=RED, parent=parent_node, left=self.NIL_LEAF, right=self.NIL_LEAF)
                self._rebalance_node(parent_node.left)
            else:
                self._insert(value, parent_node.right)

        else:
            raise ValueError('Value already in tree, try another one!')

    def _rebalance_node(self, node):  
            while node.parent.color == RED:
                if node.parent == node.parent.parent.left:
                    y = node.parent.parent.right
                    if y.color == RED:
                        node.parent.color = BLACK                           # case 1
                        y.color = BLACK                                     # case 1
                        node.parent.parent.color = RED                      # case 1
                        node = node.parent.parent                           # case 1
                    elif node == node.parent.right:
                            node = node.parent                              # case 2
                            _left_rotate(self, node)                        # case 2
                    else:                                               
                            node.parent.color = BLACK                       # case 3
                            node.parent.parent.color = RED                  # case 3
                            _right_rotate(self, node.parent.parent)         # case 3
                else: # same thing but with 'right' and 'left' exchanged
                    y = node.parent.parent.left
                    if y.color == RED:
                        node.parent.color = BLACK                           # case 1
                        y.color = BLACK                                     # case 1
                        node.parent.parent.color = RED                      # case 1
                        node = node.parent.parent                           # case 1
                    elif node == node.parent.left:
                            node = node.parent                              # case 2
                            _right_rotate(self, node)                       # case 2
                    else:                    
                            node.parent.color = BLACK                       # case 3
                            node.parent.parent.color = RED                  # case 3
                            _left_rotate(self, node.parent.parent)          # case 3
            self.root.color = BLACK

    def remove(self, value):
        if self.root:
            return _remove(self.find(value))
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')

    def _remove(self):
        pass    
        
    def height(self, node):
        if self.root:
            return self._height(self.root, 0)
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')

    def _height(self, cur_node, cur_height):
        if not cur_node:
            return cur_height
        left_height=self._height(cur_node.left, cur_height + 1)
        right_height=self._height(cur_node.right, cur_height + 1)
        return max(left_height,right_height)

    def black_height(self, node):
        if self.root:
            return self._black_height(self.root, 0)
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')
            
    def _black_height(self, cur_node, cur_black_height):
        if not cur_node:
            return cur_black_height

        # If the node's color is black, the function increments it's black_height.
        if cur_node.color == BLACK:
            left_height=self._black_height(cur_node.left, cur_height + 1)
            right_height=self._black_height(cur_node.right, cur_height + 1)
        # If the node's color is red, the function goes on to the next node without changing it's black_height.
        else:
            left_height=self._black_height(cur_node.left, cur_height)
            right_height=self._black_height(cur_node.right, cur_height)
        return max(left_black_height, right_black_height)

    def find(self, value):
        if self.root != self.NIL_LEAF:
            return _find(value)
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')

    def _find(self, value):
        cur_node = self.root
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left:
            return self._find(value, cur_node.left)
        elif value >  cur_node.value and cur_node.right:
            return self._find(value, cur_node)
        else:
            print('Sorry, value not found!')

    def search(self, value):
        if self.root:
            return self._search(value)
        else:
            return ValueError('The tree is empty! Try again after inserting some values in it.')

    def _search(self, value):
        cur_node = self.root
        if value == self.root.value:
            return True
        elif value < cur_node.value and cur_node.left:
            return self._search(value, cur_node.left)
        elif value >  cur_node.value and cur_node.right:
            return self._search(value, cur_node)
        else:
            return False

    def _inspect_insertion(self, cur_node, path=[]):
        pass

    def _inspect_removal(self, cur_node):
        pass

    

    def _left_rotate(self, node):
        other_node = node.right
        node.right = other_node.left
        if other_node.left != self.NIL_LEAF:
            other_node.left.parent = node
        if node.parent == self.NIL_LEAF:
            self.root = other_node
        elif node == node.parent.left:
            node.parent.left = other_node
        else:
            node.parent.right = other_node
        other_node.left = node
        node.parent = other_node        

    def _right_rotate(self, node):
        other_node = node.left
        node.left = other_node.right
        if other_node.right != self.NIL_LEAF:
            other_node.right.parent = node
        if node.parent == self.NIL_LEAF:
            self.root = other_node
        elif node == node.parent.right:
            node.parent.right = other_node
        else:
            node.parent.left = other_node
        other_node.right = node
        node.parent = other_node

        

        

a = RedBlackTree()


