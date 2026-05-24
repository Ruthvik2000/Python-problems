class Solution:
    def bottomView(self, root):
        d={}
        level=0
        vdis=0
        def view(node,vdis,level,d):
            if node is None:
                return None 
            if vdis not in d:
                d[vdis]=[node.data,level]
            elif vdis in d and d[vdis][1]<=level:
                d[vdis]=[node.data,level]
            view(node.left,vdis-1,level+1,d)
            view(node.right,vdis+1,level+1,d)
        
        view(root,vdis,level,d)
        dic=d
        y=[]
        for i in sorted(dic.keys()):
            y.append(dic.get(i)[0])
        return y
"""
Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 40 20 60 30
"""
