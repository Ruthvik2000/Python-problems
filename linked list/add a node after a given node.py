class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head==None:
            print("there is no linked list")
        else:
            n=self.head
            while(n!=None):
                print(n.data,"-->",end=" ")
            n=n.next
    def add_begin(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def add_after(self,data,x):#x is the node which we take to add the new_node after x
        n = self.head#n points to the node stored in the head i.e fisrt node
        while n != None:
            if x==n.data:
                break
            n = n.next#here we are pointing the next all nodes 
        if n is None:#if we dont find x in the LL then
            print("node is not presesnt in LL")
        else:
            new_node = node(data)
            new_node.next= n.next#here n is the x ,where here new_node points to the node  which was pointing by x
            n.next = new_node#here we are storing the x ref as the new node
LL=linkedlist()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(40)
LL.add_after(50,20)#we want to add 50 after 20
LL.print_LL()

""" 
output:
40-->20-->50-->10
"""