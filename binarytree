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
                inserted = BinarySearchTreeSet(element)
            else:
                self.left = self.left.insertElement(element)
                inserted = True
        elif element > self.key:
            if self.right is None:
                inserted = BinarySearchTreeSet(element)
            else:
                self.right = self.right.insertElement(element)
                inserted = True
            
        return inserted
            
    
    def searchElement(self, element):     
        found = False
        if self.key is not None:
            if self.key == element:
                found = True
            if element < self.key:
                if self.left:
                    found = self.left.searchElement(element)
                else:
                    found = False
            if element > self.key:
                if self.right:
                    found = self.right.searchElement(element)
                else:
                    found = False  
        return found
