class node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None 
root=node(10)
print(root.lchild)
print(root.rchild)

"""
output:
10
None
None
"""
root.lchild=node(5)
print(root.lchild.data)
print(root.lchild.lchild)
print(root.lchild.rchild)
"""
5
None
None
"""
root=node(10)
root.lchild=node(5)
print(root.data)
print(root.lchild)
print(root.rchild)
print(root.lchild.data)
print(root.lchild.lchild)
print(root.lchild.rchild)

"""
10
<__main__.node object at 0x7f91ae711c70>
None
5
None
None

"""