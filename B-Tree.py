class Node(object):
    def __init__(self, n=0, isleaf=True):
        self.n = n  # the number of keys in Node n
        self.keys = []  # key value
        self.childs = []  # child node
        self.leaf = isleaf  # check if leaf node

    def allocate_node(self, key_max):
        node = Node()
        child_max = key_max + 1
        # initialise key and child
        for i in range(0, key_max):
            node.keys.append(None)
        for i in range(0, child_max):
            node.childs.append(None)
        return node


class BTree(object):
    def __init__(self, t, root=None):
        self.t = t  # the minimum degree of tree
        self.max_key = 2 * self.t - 1  # the maximum number of keys in one node
        self.max_child = self.max_key + 1  # the maximum number of childs node of one node
        self.root = root  # root node

    def btree_split_child(self, x, i):
        # allocate a new node to z
        z = self.new_node()
        y = x.childs[i] # get ith. node from x
        z.leaf = y.leaf  # update the new node z
        # split, y:[1,2,3,4,5] => y:[1,2]<-[3]->[4,5]:z
        z.n = self.t - 1
        for j in range(self.t - 1):
            z.keys[j] = y.keys[j + self.t]
        if not y.leaf:
            for j in range(self.t):
                z.childs[j] = y.childs[j + self.t]

        # the number of keys of y should become t - 1
        y.n = self.t - 1
        # insert z, z becomes the first child of x
        for j in range(x.n + 1, i, -1):
            x.childs[j] = x.childs[j - 1]
        x.childs[i + 1] = z
        # grab the medium key of y to x
        for j in range(x.n, i - 1, -1):
            x.keys[j] = x.keys[j - 1]
        x.keys[i] = y.keys[self.t - 1]
        x.n = x.n + 1  # [the number of keys of x] +1


    def btree_insert_nonfull(self, x, k):
        # insert k into the x if x is non-full
        i = x.n
        # if x is leaf, insert
        if x.leaf:
            while i >= 1 and k < x.keys[i - 1]:
                x.keys[i] = x.keys[i - 1]
                i -= 1
            x.keys[i] = k
            x.n += 1
        else:
            while i >= 1 and k < x.keys[i - 1]:
                i = i - 1
            i = i + 1
            # check if down to a full child node
            if x.childs[i - 1].n == 2 * self.t - 1:
                self.btree_split_child(x, i - 1)
                # determine which child node is correct
                if k > x.keys[i - 1]:
                    i += 1
            # insert k into the root node
            self.btree_insert_nonfull(x.childs[i - 1], k)

    def new_node(self): #create node for B-Tree
        return Node().allocate_node(self.max_key)

    def btree_insert(self, k):
        if self.root is None: # check if the tree is null
            node = self.new_node()
            self.root = node
        r = self.root
        # root node is full
        if r.n == 2 * self.t - 1:
            # s = Node()
            s = self.new_node()
            # s is the new root node
            self.root = s
            s.leaf = False
            s.n = 0
            s.childs[0] = r
            # split the root node: [x,y,z] -> [x]<-[y]->[z]
            self.btree_split_child(s, 0)
            self.btree_insert_nonfull(s, k)
        else:
            self.btree_insert_nonfull(r, k)

    def walk(self):
        n = -1
        current = [self.root]
        while current:
            next_current = []
            output = []
            for node in current:
                #print(node)
                if node != None and node.childs:
                    next_current.extend(node.childs)
                if node != None:
                    output.append(node.keys[0:node.n])
            n = n + 1
            print(n,output)
            current = next_current

    # search
    def search(self, x, k):
        i = 0
        #print(i, x.n, k, x.keys[i])
        # print(x)
        # print(x.keys[i])
        #key = x.keys[i]
        while x.keys[i] != None and i <= x.n and k > x.keys[i]:
            i += 1
            key = x.keys[i]
        if i < x.n and k == x.keys[i]: # check if found
            return (x, i)
        # not found but at leaf node
        elif x.leaf:
            return None
        # not found and not at the leaf node, continue to search
        else:
            return self.search(x.childs[i], k)

def to_read():
    file = open(input("enter the file name: "), "r")
    array = []
    for line in file:
        for word in line.split():
            array.append(str(word))
    print(array)
    return array

array = to_read()
array = list(set(array))
tree = BTree(5)
for x in array:
    tree.btree_insert(x)

# output the B-tree
tree.walk()
print('\n')
# search
search = input("Enter the search key:")
result = tree.search(tree.root, search)
if result != None:
    print("find:" + result[0].keys[result[1]])
else:
    print("not find key")