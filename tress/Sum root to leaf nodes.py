# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # @param A : root node of tree
    # @return an integer

    def sumNumbers(self, root):
        final=[]
        def helper(node,string):
            if node is not None:
                if node.left is None and node.right is None:
                    final.append(int(string+str(node.val)))
                    return
                else:
                    helper(node.left, string+str(node.val))
                    helper(node.right, string+str(node.val))
        helper(root," ")
        x=sum(final)
        return x 

"""
Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.

The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
"""