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
    def search(self,y):
        if self.key==None:
            print("tree is not there")
        if self.key==y:
            print("The key is the root w.r.t the sub tree or the tree and its present")
            return
        if self.key>=y:
            if self.lchild==None:
                print("there is no lchild and there is no key")
            else:   #or if self.lchild:
                self.lchild.search(y) 
        else:
            if self.rchild==None:
                print("there is no key because there is no right child")
            else:
                self.rchild.search(y)
root=node(10)
a=[6,3,1,6,98,3,7]
for i in a:
    root.insert(i)
root.search(1)

"""
output:
 print("The key is the root w.r.t the sub tree or the tree and its present")
"""