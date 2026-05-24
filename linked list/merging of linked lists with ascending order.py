# A single node of a singly linked list
class node:
  def __init__(self,data):#creation of just single node not pointing to other nodes
        self.data=data
        self.next=None
class LinkedList:
  def __init__(self):  
    self.head = None
  def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node#if there is no linked list then we are storing the new node address in the head
        else:#if there is existence of LL
            n=self.head#points to the address of the node in the list
            while(n.next != None):
                n=n.next#here we will get the address of the last node after execution of the last node
            n.next=new_node#here
  # print method for the linked list
  def print_LL(self):
        if self.head==None:
            print("there is no linked list")
        else:
            n=self.head
            while(n!=None):
                print(n.data,"-->",end=" ")
#-----------------------Merge function---------------------#
  def merge(List_1, List_2):
    # Node for output LinkedList
    head_ptr = n = node() 
    # head_ptr will be the head node of the output list 
    # n will be used to insert nodes in the output list
    # Loop for merging two lists
    # Loop terminates when both lists reaches to its end
    while List_1 and List_2:
        # List_1 has not reached its end
        # and List_2 has either reached its end or its current node has data
        # greater than or equal to the data of List_1 node
        # than insert List_1 node in the ouput list
        if List_1 and (not List_2 or List_1.data <= List_2.data):
            n.next = node(List_1.data)
            List_1 = List_1.next
        # otherwise insert List_2 node in the ouput list
        else:
            n.next = node(List_2.data)
            List_2 = List_2.next
        # move temp_pointer to next position
        n=n.next
    # return output list
    return head_ptr.next

#1 st list
LL1 = LinkedList()
LL1.insert(1)
LL1.insert(2)
LL1.insert(4)
# Linked List with odd numbers
LL2 = LinkedList()
LL2.insert(1)
LL2.insert(3)
LL2.insert(4)
# Merge Function
LL3 = LinkedList()
LL3.head=merge(LL1.head,LL2.head)
LL3.printLL()