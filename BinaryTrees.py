class Node:
    def __init__(self,val):
        self.right = None 
        self.left = None
        self.data = val

#insert values into a tree
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# print a tree    ""same as inorder tree tarversal technique""
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

#tree traversal techniques:
#  Inorder : left--> node data--> right
    def inordertraversal(self,root):
        r=[]
        if root:
            r = self.inordertraversal(root.left)
            r.append(root.data)
            r = r + self.inordertraversal(root.right)
        return r


    #  Preorder : node data--> left --> right
    def preordertraversal(self,root):
        r=[]
        if root:
            r.append(root.data)
            r = r + self.inordertraversal(root.left)
            r = r + self.inordertraversal(root.right)
        return r


    #  Postorder : left --> right -->node data
    def postordertraversal(self,root):
        r=[]
        if root:
            r = r + self.inordertraversal(root.left)
            r = r + self.inordertraversal(root.right)
            r.append(root.data)
        return r

    # find a value in a tree given
    def findval(self,key):
        if key < self.data:
            if self.left is None:
                return str(key)+ " not found "
            else:
                return self.left.findval(key)
        elif key > self.data:
            if self.right is None:
                return str(key) + " not found "
            else:
                return self.right.findval(key)
        else: 
            return str(self.data)+" is found"
    
root = Node(12)
root.insert(6)
root.insert(16)
root.insert(3)
root.insert(34)
root.printTree()
print(root.inordertraversal(root))
print(root.preordertraversal(root))
print(root.postordertraversal(root))
p = root.findval(39)
print(p)









