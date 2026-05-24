class Node:
    def __init__(self,data):#creation of just single node not pointing to other nodes
        self.data=data
        self.next=None
class linkedlist:
    #function to create head
    def __init__(self):
        self.head=None#it means  intialy we had a empty linked list,where generelly head points to the first node of linked list
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head#taking the new node(inserted at the begging of the LL)ref as the ref stored in head(which was the actual first node )
        self.head= new_node#after creatinf the new node we are making the add of new node need to be stored in head
    def print_LL(self):
        if self.head==None:
            print("linked list is empty")
        else:
            n=self.head# n is like a temp
            while n != None:
                print(n.data,"-->",end=" ")
                n=n.next
    def add_before(self,data,x):
        if self.head == None:
            return("Linked List is empty!")
        if self.head.data==x:#it means if the x is the first node,then this if statement works and self.head.data points to the data of the address stored in the head
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return#it means the process will be ended
        #from if x is not the first node the following process will continue
        n = self.head
        while n.next != None:
            if n.next.data==x:"""
                                 n.ref.data pointing to the next node data if it is equal to the given data=x then the new node will
                                 inserted in b/w n.data ,n.next.data
                                """
            break
            n = n.next        
        if n.next == None:#(it means there is node to point out)
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node    
LL=linkedlist()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(40)
LL.add_before(60,20)
"""
outut:
40-->60-->20-->10
"""