class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self,root, B):
        depth=0
        parent=None 
        info=[]
        xinfo=[]
        ans1=self.search(root,B,depth,parent,info)
        finddepth=ans1[0][0]
        ndepth=0
        ans2=self.find(root,finddepth,ndepth,parent,xinfo)
        ans3=[]
        for i in ans2:
            if i[0][1]!=ans1[0][1] and i[0][2]!=ans1[0][2]:
                ans3.append(i[0][2])
        return ans3
    def search(self,node,B,depth,parent,info):
        if node is None:
            return []
        if node.val==B:
            info.append((depth,parent,nod.val))
        self.search(node.left,B,depth+1,node,info)
        self.search(node.right,B,depth+1,node,info)
        return info
    def find(self,node,finddepth,ndepth,parent,xinfo):
        if node is None:
            return []
        if ndepth==finddepth:
            xinfo.append((ndepth,parent,node.val))
        self.find(node.left,finddepth,ndepth+1,node,xinfo)
        self.find(node.right,finddepth,ndepth+1,node,xinfo)
        return xinfo