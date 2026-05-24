class Node:
    def __init__(self,data):#creation of just single node not pointing to other nodes
        self.data=data
        self.next=None
class linkedlist:
    #function to create head
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head==None:
            print("linked list is empty")
        else:
            n=self.head# n is like a temp
            while n != None:
                print(n.data)
                n=n.next
li=linkedlist()
li.print_LL()
