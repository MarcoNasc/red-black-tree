## Red-black Tree implemented in Python 3.x

from node import *

# Usual functions are used to check if there is a root in the tree
# and to call their pair "private" _function. Those two parts could be brought together,
# but are divided for organization purposes.

class RedBlackTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if not self.root:
            return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
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

                if n.value != None:
                    buf = ' ' * int((5 - len(str(n.value))) / 2)
                    if n.color == RED:
                        cur_row += f'{buf}{RED, str(n.value)}{buf}' + sep
                    elif n.color == BLACK:
                        cur_row += f'{buf}{BLACK, str(n.value)}{buf}' + sep
                        
                else:
                    cur_row += ' ' * 5 + sep

                if n.left_child != None:
                    next_nodes.append(n.left_child)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right_child != None:
                    next_nodes.append(n.right_child)
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
            self.root = Node(value, color=BLACK, parent=None)
        else:
            self._insert(value, self.root)

    def _insert(self, value, parent_node):
        if value < parent_node.value:
            if not parent_node.left:
                parent_node.left = Node(value, color=RED, parent=parent_node)
            #    self._inspect_insertion(parent_node.left)
            else:
                self._insert(value, parent_node.left)

        elif value > parent_node.value:
            if not parent_node.right:
                parent_node.right = Node(value, color=RED, parent=parent_node)
            #    self._inspect_insertion(parent_node.right)
            else:
                self._insert(value, parent_node.right)

        else:
            raise DuplicateValueError('Value already in tree, try another one!')

    def remove(self, value):
        if self.root:
            return _remove(self.find(value))
        else:
            raise EmptyTreeError('The tree is empty! Try again after inserting some values in it.')

    def _remove(self):
        pass    
        
    def height(self):
        if self.root:
            return self._height(self.root, 0)
        else:
            raise EmptyTreeError('The tree is empty! Try again after inserting some values in it.')

    def _height(self, cur_node, cur_height):
        if not cur_node:
            return cur_height
        left_height=self._height(cur_node.left, cur_height + 1)
        right_height=self._height(cur_node.right, cur_height + 1)
        return max(left_height,right_height)

    def black_height(self):
        if self.root:
            return self._black_height(self.root, 0)
        else:
            raise EmptyTreeError('The tree is empty! Try again after inserting some values in it.')
            
    # Black Height has a similar concept of the commom Height, the difference is that it only counts the black nodes.
    def _black_height(self, cur_node, cur_black_height):
        if not cur_node:
            return cur_black_height

        # If the node's color is black, the function increments it's black_height.
        if cur_node.color = BLACK
            left_height=self._black_height(cur_node.left, cur_height + 1)
            right_height=self._black_height(cur_node.right, cur_height + 1)
        # If the node's color is red, the function goes on to the next node without changing it's black_height.
        else:
            left_height=self._black_height(cur_node.left, cur_height)
            right_height=self._black_height(cur_node.right, cur_height)
        return max(left_black_height, right_black_height)

    def find(self, value):
        if self.root:
            return _find(value)
        else:
            raise EmptyTreeError('The tree is empty! Try again after inserting some values in it.')

    def _find(self, value):


    def search(self):
        pass

    def _search(self):
        pass

    def _inspect_insertion(self, cur_node, path=[]):
        pass

    def _inspect_deletion(self, cur_node):
        pass

    def _rebalance_node(self, z, y, x):
        pass

    def _left_rotation(self):
        pass

    def _right_rotation(self):
        pass

