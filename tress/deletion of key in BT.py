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
    def deletion(self,x):
        if self.key==None:
            print("There is no root")
        if self.key>x:
            if self.lchild:
                self.lchild=self.lchild.deletion(x) #here the self.lchild.deletio(x) will return a value
                                                    #the result will the adress of the x i.e None because after deletion there will no data that means there will be no address
                                                    #and that result i.e None will be stored at the lchild of the key w.r.t suntree or tree
            else:
                print("there is no lchild ,So we cant find and del the node")
                return
        if x>self.key:
            if self.rchild:
                self.rchild=self.rchild.deletion(x)
            else:
                print("there is no rchild")
                return
        else:   #it means self.key==x--> means self is pointing to the node which want to delete
                #Now the steps are to delete the node w.r.t 3 cases
                #case1 : if the node contains no child i.e a leaf node 
                #case2 : if the node contains 1 child 
                #case3 : if the node cotains 2 childs
            if self.lchild is None:
                temp=self.rchild
                self=None  #it means deletes the node 
                return temp #return the last recursion node and stores the rchild as its node in place of node which we deleted
            if self.rchild is None:
                temp=self.lchild
                self=None 
                return temp
            #the two if statemts applicable for the case1,case2
            #if there are 2 childs to the node which we want to delete,then
            #then there will be 2 cases
            """
            possibility 1 : we can replace the node which we want to delete with the max key of the left sub tree of the node,
            possibility 2 : we can replace it with the min key of the right sub tree of the node
            """
            #whatever it may be the max,min key's will be present at the leaf nodes ,to get them we nedd to run a while loop

            #if we select right sub tree
            node=self.rchild 
            while node.lchild: #to find the min in the right subtree we will run through lift child's of the node till we founf leaf at left position
                node=node.lchild #here we got the min of left sub tree and pointing it with node
            self.key=node.key #here we replaced the deletion key with the min 
                              #Now we need delete the duplicate node i.e at the leaf position that will be at right subtree which was the choosen path
            self.rchild=self.rchild.deletion(node.key)
        return self 
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.key:
            print(self.key)
        if self.rchild:
            self.rchild.inorder()
root=node(10)
a=[6,3,1,6,98,3,7]
for i in a:
    root.insert(i)
root.inorder()
root.deletion(10)
print("\n")
root.inorder()


"""
1
3
6
7
8
10
98


1
3
6
7
8
98

"""
        