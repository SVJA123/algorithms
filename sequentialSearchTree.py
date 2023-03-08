class SequentialSearchSet(AbstractSet):
    
    def __init__(self):
        # ADD YOUR CODE HERE
        self.array = []        
     
    
        
    def insertElement(self, element):
        inserted = False
        # ADD YOUR CODE HERE
        #for i in len(self.array):
        #    if element < self.array[i]:
        #        self.array.insert(i, element)
        #        inserted = True
        #        break
        if element in self.array:
            inserted = False
        else:
            self.array.append(element)
            inserted = True
        return inserted
    
    

    def searchElement(self, element):     
        found = False
        # ADD YOUR CODE HERE
        for i in self.array:
            if i == element:
                found = True
                break
        
        return found

ar = SequentialSearchSet()
ar.array = [4, 7, 9, 1]
print(ar.insertElement(9))
print(ar.searchElement(5))
