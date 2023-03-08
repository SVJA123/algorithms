from bitarray import bitarray

class BloomFilterSet(AbstractSet):
    def __init__(self, word_num=0):
        # ADD YOUR CODE HERE
        # initialize an empty bitarray
        bit_num = int(-word_num*(self.ln(0.001)) / (self.ln(2)**2))
        self.num_hashes = int(bit_num / word_num * self.ln(2))
        self.bitfield = bitarray(bit_num)
        self.bitfield.setall(0)
    
    @staticmethod
    def ln(x):
        n = 1000.0
        return n * ((x ** (1/n)) - 1)
    
    def get_index(self, key):
        return hash(key) % len(self.bitfield)
        
    def insertElement(self, element):
        # ADD YOUR CODE HERE
        for i in range(self.num_hashes):
            index = self.get_index(element + str(i))
            self.bitfield[index] = True
        return True
    

    def searchElement(self, element):     
        # ADD YOUR CODE HERE
        for i in range(self.num_hashes):
            index = self.get_index(element + str(i))
            if not self.bitfield[index]:
                return False
        return True
        
file = open(input("enter the file name: "), "r")
data = file.read().split()
bf = BloomFilterSet(len(data))
for word in data:
    bf.insertElement(word)
file.close()

print(bf.searchElement("always"))
print(bf.searchElement("alexio"))
print(bf.searchElement("david"))
print(bf.searchElement("eight"))
print(bf.searchElement("alcohol"))
