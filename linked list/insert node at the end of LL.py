class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        new_node=node(data)
        new_node.next=self.head#taking the new node(inserted at the begging of the LL)ref as the ref stored in head 
        self.head= new_node#after creating the new node we are making the add of new node need to be stored in head
    def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node#if there is no linked list then we are storing the new node address in the head
        else:#if there is existence of LL
            n=self.head#points to the address of the node in the list
            while(n.next != None):
                n=n.next#here we will get the address of the last node after execution of the last node
            n.next=new_node#here we storing the last next to refer the new node ,then the new node will become last node
    def print__LL(self):
        if self.head==None:
            print("linked list is empty")
        else:
            n=self.head
            while(n!=None):
                print(n.data,"-->",end=" ")#executes in the same line
                n=n.next
LL=linkedlist()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(40)
LL.add_end(50)
LL.print__LL()

"""
output:
40 -->20-->10-->50-->
"""