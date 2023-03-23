class newNode():
    def __init__(self,value):
        self.data = value
        self.next = None
class Link():
    def __init__(self):
        self.head = None
    def create(self,x):
        if (self.head == None):
            self.head = newNode(x)
        else:
            self.temp = self.head
            while(self.temp.next!=None):
                self.temp=self.temp.next
            self.temp.next = newNode(x)
    def print(self,head):
        self.temp=self.head
        while(self.temp!=None):
            print(self.temp.data)
            self.temp = self.temp.next
L1=Link()     # creating object for linked list 
L1.create(10) # creating a head node with data value 10
L1.create(20)
L1.create(30)
L1.create(40)
L1.create(50)
L1.print(10) # printing a linked list  using head value

