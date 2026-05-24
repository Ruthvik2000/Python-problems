#creation of a node with arguments data,next intilazing them with None
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
# A Linked List class with a single head node
class linkedlist:
    # Function to initialize head 
    def __init__(self,head=None):
        self.head=head
# Code execution starts here 
if __name__=="__main__"
a=node(1)#1 is the data of node a .where we took a as an object
b=node(2)#2 is the data of node b
c=node(3)#3 is the data of node c
#Now we need to create a linked list by connecting a to b,b to c using next variable in node class
#first we need to set the head of the linked list
#for this we need to create a object (OR) constructor to the linkedlist class  to access the __init__ funnction
li=linkedlist()
li.head=a 
#li=linkedlist(a)
#now create links in between the nodes
a.next=b
b.next=c