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
    def sumn(self,root):#here root is the root node
        if self.root is None:
            return 0
        else:
            leftsum = sumn (root.lchild)
            rightsum = sumn (root.rchild)
            return(root.data+leftsum+rightsum)
k=node(10)
a=[6,3,1,98,7]
for i in a:
    k.insert(i)
h=node()
h.sumn(k)
