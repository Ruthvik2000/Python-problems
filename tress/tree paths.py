class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def traverse(node, string):
            if node == None:
                return
            if node.left == None and node.right == None:
                res.append(string+str(node.val))
                return 
            traverse(node.left, string + str(node.val) + "->")
            traverse(node.right, string + str(node.val) + "->")
        
        traverse(root, "")
        return res

"""
    1
   / \
  2   3
  Input:root=[1,2,3]
  Output:["1->2","1->3"]
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""