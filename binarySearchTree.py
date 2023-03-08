class BinarySearchTreeSet(AbstractSet):
    
    def __init__(self, key=None):
        # ADD YOUR CODE HERE
        self.key = key
        self.left = None
        self.right = None
             
    
        
    def insertElement(self, element):
        inserted = False
        # ADD YOUR CODE HERE
        if not self.key:
            self.key = BinarySearchTreeSet(element)
            inserted = True
            return inserted
        
        if self.key == element:
            inserted = False
            return inserted
        
        if element < self.key:
            if self.left:
                inserted = self.left.insertElement(element)
            else:
                self.left = BinarySearchTreeSet(element)
                inserted = True
                return inserted
        elif element > self.key:
            if self.right:
                inserted = self.right.insertElement(element)
            else:
                self.right = BinarySearchTreeSet(element)
                inserted = True
                return inserted
      
        
        return inserted
    
    

    def searchElement(self, element):     
        found = False
        # ADD YOUR CODE HERE
        if self.key == element:
            found = True
        if element < self.key:
            if self.left:
                found = self.left.searchElement(element)
            else:
                found = False
                return found
        elif element > self.key:
            if self.right:
                found = self.right.searchElement(element)
            else:
                found = False
                return found

        return found 

file = open(input("enter the file name: "), "r")
data = file.read().split()
tree = BinarySearchTreeSet(data[0])
for num in range(1, len(data)):
    tree.insertElement(data[num])
file.close()
