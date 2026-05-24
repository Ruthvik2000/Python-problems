# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        q=[(root,0)]
        width=1
        while len(q)!=0:
            if len(q)>1:
                width=max(width,q[-1][1]-q[0][1]+1)
            temp_q=[]
            while len(q)!=0:
                node,position=q.pop(0)
                if node.left:
                    temp_q.append((node.left,position*2+1))
                if node.right:
                    temp_q.append((node.right,position*2+2))
            q=temp_q 
        return width
                