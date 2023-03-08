class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.right = None
        self.parent = None
        self.color = "RED"          
        
class BalancedSearchTreeSet(AbstractSet):
    #initialize the tree
    def __init__(self):
        self.root = None

    def insertElement(self, element):
        inserted = False
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.root.color = "black"
            return

        # Insert node like in BST
        curr_node = self.root
        while True:
            if value < curr_node.value:
                curr_node.
                if curr_node.left is None:
                    curr_node.left = new_node
                    new_node.parent = curr_node
                    break
                else:
                    curr_node = curr_node.left
            elif value > curr_node.value:
                if curr_node.right is None:
                    curr_node.right = new_node
                    new_node.parent = curr_node
                    break
                else:
                    curr_node = curr_node.right
            else:
                return  # If duplicate value is already present

        # Fix Red-Black Tree properties
        self._insert_up(new_node)
        
        
    def _insert_up(self, node):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.rotate.right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.rotate_left(node.parent.parent)
        self.root.color = 'black'

        
    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.nil:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

        
    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.nil:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child
        left_child.right = node
        node.parent = left_child
        

    def get(self, val):
        curr_node = self.root
        while curr_node != self.nil:
            if curr_node.val == val:
                return True
            elif val < curr_node.val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return False
