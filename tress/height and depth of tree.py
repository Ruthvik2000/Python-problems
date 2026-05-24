#Depth calculation 
#We assume that empty node means depth 0 ,asd the tree with  single node is 1
class Solution:
	# @param A : root node of tree
	# @return an integer
	def maxDepth(self, A):
        def helper(node):
            if not node:
                return 0
            if node:
                return 1+max(helper(node.left), helper(node.right))     
        return helper(A)   
 


#Height Calculation
#We assue that empty node means height -1 and the tree with single node is 0
class Solution:
	# @param A : root node of tree
	# @return an integer
	def height(self, A):
        def helper(node):
            if not node:
                return -1
            if node:
                return max(helper(node.left), helper(node.right))+1     
        return helper(A)   
 