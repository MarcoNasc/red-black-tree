# Red-black Tree implemented in Python 3.x

from node import *

# Usual functions are used to check if there is a root in the tree
# and to call their pair "private" _function. Those two parts could be brought together,
# but are divided for organization purposes.
    
class RedBlackTree:
    
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
        if not self.root:
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
                        # cur_row += f"{buf}{RED[0], str(n.value)}{buf}" + sep
                        cur_row += '{}{}{}'.format(buf, RED[0]+str(n.value), buf) + sep
                    elif n.color == BLACK:
                        # cur_row += f"{buf}{BLACK[0], str(n.value)}{buf}" + sep
                        cur_row+='{}{}{}'.format(buf, BLACK[0]+str(n.value), buf)+  sep

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
        if not self.root:
            self.root = Node(value, color=BLACK, parent=self.NIL_LEAF, left=self.NIL_LEAF, right=self.NIL_LEAF)
        else:
            self._insert(value, self.root)

    def _insert(self, value, parent_node):
        
        if value < parent_node.value:
            if not parent_node.left:
                parent_node.left = Node(value, color=RED, parent=parent_node, left=self.NIL_LEAF, right=self.NIL_LEAF)
                self._fixup_insertion(parent_node.left)
            else:
                self._insert(value, parent_node.left)

        elif value > parent_node.value:
            if not parent_node.right:
                parent_node.right = Node(value, color=RED, parent=parent_node, left=self.NIL_LEAF, right=self.NIL_LEAF)
                self._fixup_insertion(parent_node.right)
            else:
                self._insert(value, parent_node.right)

        else:
            raise ValueError('Value already in tree, try another one!')        

    def _fixup_insertion(self, node):  
            while node.parent.color == RED:
                if node.parent == node.parent.parent.left:
                    y = node.parent.parent.right
                    if y.color == RED:
                        node.parent.color = BLACK                           
                        y.color = BLACK                                     
                        node.parent.parent.color = RED                      
                        node = node.parent.parent                           
                    else:
                        if node == node.parent.right:
                            node = node.parent                              
                            self._left_rotate(node)                                                                    
                        node.parent.color = BLACK                           
                        node.parent.parent.color = RED                      
                        self._right_rotate(node.parent.parent)              
                else: # same thing but with 'right' and 'left' exchanged
                    y = node.parent.parent.left
                    if y.color == RED:
                        node.parent.color = BLACK                           
                        y.color = BLACK                                     
                        node.parent.parent.color = RED                      
                        node = node.parent.parent                           
                    else:
                        if node == node.parent.left:
                            node = node.parent                              
                            self._right_rotate(node)                        
                        node.parent.color = BLACK                           
                        node.parent.parent.color = RED                      
                        self._left_rotate(node.parent.parent)               
            self.root.color = BLACK
            print(self)

    def delete(self, value):
        if self.root:
            return self._delete(self.find(value))
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')

    def _delete(self, node):
        other_node = node
        other_node_original_color = other_node.color
        if not node.left:
            third_node = node.right
            self._transplant(node, node.right)
        elif not node.right:
            third_node = node.left
            self._transplant(node, node.left)
        else:
            other_node == self._minimum_node(node.right)
            other_node_original_color = other_node.color
            third_node = other_node.right
            if other_node.parent == node:
                third_node.parent = other_node
            else:
                self._transplant(other_node, other_node.right)
                other_node.right = node.right
                other_node.right.parent = other_node
            self._transplant(node, other_node)
            other_node.left = node.left
            other_node.left.parent = other_node
            other_node.color = node.color
        if other_node_original_color == BLACK:
            self._fixup_deletion(third_node)
        print(self)


    def _fixup_deletion(self, node):
        while node != self.root and node.color == BLACK:
            if node == node.parent.left:
                other_node = node.parent.right
                if other_node.color == RED:
                    other_node.color == BLACK
                    node.parent.color = RED
                    self._left_rotate(node.parent)
                if other_node.left.color == BLACK and other_node.right.color == BLACK:
                    other_node.color = RED
                    node = node.parent
                else:
                    if other_node.right.color == BLACK:
                        other_node.left.color == BLACK
                        other_node.color == RED
                        self._right_rotate(other_node)
                    other_node.color = node.parent.color
                    node.parent.color = BLACK
                    other_node.right.color = BLACK
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                other_node = node.parent.left
                if other_node.color == RED:
                    other_node.color == BLACK
                    node.parent.color = RED
                    self._right_rotate(node.parent)
                if other_node.right.color == BLACK and other_node.left.color == BLACK:
                    other_node.color = RED
                    node = node.parent
                else:
                    if other_node.left.color == BLACK:
                        other_node.right.color == BLACK
                        other_node.color == RED
                        self._left_rotate(other_node)
                    other_node.color = node.parent.color
                    node.parent.color = BLACK
                    other_node.left.color = BLACK
                    self._right_rotate(node.parent)
                    node = self.root
        node.color = BLACK


    def _transplant(self, node, other_node):
        if not node.parent:
            self.root = other_node
        elif node == node.parent.left:
            node.parent.left = other_node
        else:
            node.parent.right = other_node
        other_node.parent = node.parent

    def maximum(self):
        if self.root:
            return self._maximum(self.root)
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')

    def _maximum(self, node):
        while node.right:
            node = node.right
        return node.value

    def minimum(self):
        if self.root:
            return self._minimum(self.root)
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')

    def _minimum(self, node):
        while node.left:
            node = node.left
        return node.value

    def _mininum_node(self, node):
        while node.left:
            node = node.left
        return node

    def _maximum_node(self, node):
        while node.right:
            node = node.right
        return node
        
    def height(self, node):
        if self.root:
            return self._height(self.root, 0)
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')

    def _height(self, cur_node, cur_height):
        if not cur_node:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

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
            left_black_height = self._black_height(cur_node.left, cur_black_height + 1)
            right_black_height = self._black_height(cur_node.right, cur_black_height + 1)
        # If the node's color is red, the function goes on to the next node without changing it's black_height.
        else:
            left_black_height = self._black_height(cur_node.left, cur_black_height)
            right_black_height = self._black_height(cur_node.right, cur_black_height)
        return max(left_black_height, right_black_height)

    def find(self, value):
        if self.root:
            return self._find(value, self.root)
        else:
            raise ValueError('The tree is empty! Try again after inserting some values in it.')

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left:
            return self._find(value, cur_node.left)
        elif value >  cur_node.value and cur_node.right:
            return self._find(value, cur_node.right)
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

    def _left_rotate(self, node):
        other_node = node.right
        node.right = other_node.left
        if other_node.left:
            other_node.left.parent = node
        other_node.parent = node.parent
        if not node.parent:
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
        if other_node.right:
            other_node.right.parent = node
        other_node.parent = node.parent
        if not node.parent:
            self.root = other_node
        elif node == node.parent.right:
            node.parent.right = other_node
        else:
            node.parent.left = other_node
        other_node.right = node
        node.parent = other_node

        

        

a = RedBlackTree()
