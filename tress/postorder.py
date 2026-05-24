# root-->left sub tree nodes-->right subtree nodes 
class node:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,x): #x is the node to be inserted
        if self.key is None:
            self.key=x
            return   #if condition passes then the insertion method will end
        if self.key>=x:  #here self.key is the root node
            """
            if we do not want the duplicate values then 
            if self.key==x:
                return
            """
            if self.lchild is None:
                self.lchild=node(x)
            else:     #if lchild of the node is present then
                self.lchild.insert(x) #performing recursion,here the left node of the root node becomes root node for lsubtree and again performannce insertion
        else:
            if self.rchild is None:
                self.rchild=node(x)
            else:
                self.rchild.insert(x)
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        if self.key:
            print(self.key)
root=node(10)
a=[6,3,1,98,7]
for i in a:
    root.insert(i)
root.postorder()


"""
output:
1
3
7
6
98
10
"""