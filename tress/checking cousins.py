class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth=0
        parent=None
        xinfo=[]
        yinfo=[]
        self.helper(root,x,y,depth,parent,xinfo,yinfo)
        return xinfo[0][0]==yinfo[0][0] and xinfo[0][1]!=yinfo[0][1]
    def helper(self,node,x,y,depth,parent,xinfo,yinfo):
        if node is None:
            return False
        if node.val==x:
            xinfo.append((depth,parent))
        if node.val==y:
            yinfo.append((depth,parent))
        self.helper(node.left,x,y,depth+1,node,xinfo,yinfo)
        self.helper(node.right,x,y,depth+1,node,xinfo,yinfo)
"""
    1
   / \
   2  3
    \  \
     4  5
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
"""