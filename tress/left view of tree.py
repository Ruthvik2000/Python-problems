'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    level=0
    stack=[]
    def dfs(node,level):
        if node is None:
            return None 
        if len(stack)==level:
            stack.append(node.data)
        dfs(node.left,level+1)
        dfs(node.right,level+1)
    dfs(root,level)
    return stack


"""
Input:
   1
 /  \
3    2
Output: 1 3
"""