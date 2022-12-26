# creating a node class
class Node:
    def __init__(self,val):
        self.childleft = None
        self.childright = None
        self.nodedata = val

# creating an instance of node class to craete a tree as required
root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)

#Tree traversal techniques are 3 Inorder,pre order,postorder

#Inorder tree traversal:

def Inord(root):
    if root:
        Inord(root.childleft)
        print(root.nodedata)
        Inord(root.childright)
Inord(root)

#Preorder tree traversal:

def Preord(root):
    if root:
        print(root.nodedata)
        Preord(root.childleft)
        Preord(root.childright)
Preord(root)

#Postorder tree tarversal:

def Postord(root):
    if root:
        Postord(root.childleft)
        Postord(root.childright)
        print(root.nodedata)
Postord(root)



