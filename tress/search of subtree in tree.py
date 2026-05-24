class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is not None:
            if root.val == val:
                return root
            elif root.val > val:
                return self.searchBST(root.left, val)
            elif root.val < val:
                return self.searchBST(root.right, val)
        return None

"""
Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
"""