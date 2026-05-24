class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        curr = root
        l, r = 1, 1
        while curr.left:
            l += 1
            curr = curr.left
        curr = root
        while curr.right:
            r += 1
            curr = curr.right
        if l == r:
            return 2 ** l - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


"""
other code:
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + self.countNodes(root.right) + self.countNodes(root.left)
        
"""


"""
Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
"""