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
        x=self.helper(A,len(A),B,len(B))
        y=len(A)+len(B)
        return y-x 
a=input("enter the first string:\n")
b=input("enter the second atring:\n")
c=Solution()
print(c.solve(a,b))
"""
enter the first string:
aggtab
enter the second atring:
gxtxayb
9
"""

#that shortest common supersequence is   aggxtxayb of length 9