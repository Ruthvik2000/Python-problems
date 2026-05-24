import sys
sys.setrecursionlimit(10**9)
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def helper(self,A,n,B,m):
        if n==0 or m==0:
            return 0 
        if (n,m) in self.d:
            return self.d[(n,m)]
        if A[n-1]==B[m-1]:
            self.d[(n,m)]=self.helper(A,n-1,B,m-1)+1
            return self.d[(n,m)]
        else:
            self.d[(n,m)]=max(self.helper(A,n,B,m-1),self.helper(A,n-1,B,m))
            return self.d[(n,m)]
        return self.d[(n,m)]

    def solve(self, A, B):
        if not A or not B:
            return 0
        self.d={}
        return self.helper(A,len(A),B,len(B))
    def printsub(self,A,B):
        i=len(A)
        j=len(B)
        lst=[]
        while(i>0 and j>0):
            if A[i-1]==B[j-1]:
                lst.append(A[i-1])
                i-=1
                j-=1
            else:
                if self.d[(i,j-1)]>self.d[(i-1,j)]:
                    j-=1
                else:
                    i-=1
        lst.reverse()
        s="".join(lst)
        return s
a=input("enter the first string:\n")
b=input("enter the second atring:\n")
c=Solution()
print(c.solve(a,b))
print(c.printsub(a,b)) 


"""
enter the first string:
abbcdgf
enter the second atring:
bbadcgf
5
bbcgf
"""
