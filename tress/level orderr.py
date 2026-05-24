# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=[root]
        next_que=[]
        level=[]
        result=[]
        while queue != []:
            for i in queue:
                level.append(i.val)
                if i.left:
                    next_que.append(i.left)
                if i.right:
                    next_que.append(i.right)
            result.append(level)
            level=[]
            queue=next_que
            next_que=[]
        return result
            
            
"""
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""