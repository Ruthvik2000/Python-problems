class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):
        d={}
        hdis=0
        vdis=0
        def dfs(node,hdis,vdis,d):
            if not node:
                return None 
            if hdis not in d:
                d[hdis]=[(node.val,vdis)]
            else:
                d[hdis].append((node.val,vdis))
            dfs(node.left,hdis-1,vdis+1,d)
            dfs(node.right,hdis+1,vdis+1,d)
        dfs(A,hdis,vdis,d)
        dic=d
        res=[]
        for y in sorted(dic):
            dic[y]=sorted(dic[y],key=lambda x:x[1])
            s=[]
            for i in dic[y]:
                s.append(i[0])
            res.append(s)
        return res