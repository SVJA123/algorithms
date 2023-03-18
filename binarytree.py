class BinarySearchTreeSet(AbstractSet):
    
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None
        
    def insertElement(self, element):
        inserted = False
        if self.key is None:
            self.key = element
            inserted = True
        elif element < self.key:
            if self.left is None:
                self.left = BinarySearchTreeSet(element)
                inserted = True
            else:
                inserted = self.left.insertElement(element)
        elif element > self.key:
            if self.right is None:
                self.right = BinarySearchTreeSet(element)
                inserted = True
            else:
                inserted = self.right.insertElement(element)
        else:
            inserted = False 
        return inserted
    
    
    
    def searchElement(self, element):     
        found = False
        node = self
        while node is not None:
            if element == node.key:
                found = True
                break
            elif element < node.key:
                node = node.left
            else:
                node = node.right
        return found
