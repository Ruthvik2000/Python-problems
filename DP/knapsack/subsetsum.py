#using bottomdown

class Solution:
    def helper(self,A,B,n):
        x=[[False for j in range(B+1)]for i in range(n+1)]
        for i in range(n+1):
            x[i][0]=True
        for i in range(1,n+1):
            for j in range(1,B+1):
                if A[i-1]>j:
                    x[i][j]=x[i-1][j]
                else:
                    x[i][j]=x[i-1][j-a[i-1]] or x[i-1][j]
        return x[n][B]
        
    def subsetsum(self,A,B):
        n=len(A)
        return self.helper(A,B,n)
a=[int(a) for a in input().split()]
b=int(input("entre the number: "))      
x=Solution()
print(x.subsetsum(a,b)) 
"""
2 3 7 8 10
entre the number: 11
True

"""

#code in python using memoization
class Solution:
    def __init__(self):
        self.d={}
    def helper(self,A,B,n):
        if B==0:
            return True 
        if n==0:
            return False 
        if (n,B) in self.d:
            return self.d[(n,B)]
        if A[n-1]>B:
            self.d[(n,B)]=self.helper(A,B,n-1)
            return self.d[(n,B)]
        if A[n-1]<=B:
            self.d[(n,B)]=self.helper(A,B-A[n-1],n-1) or self.helper(A,B,n-1)
        return self.d[(n,B)]    
    def subsetsum(self,A,B):
        n=len(A)
        return self.helper(A,B,n)
a=[int(a) for a in input().split()]
b=int(input("entre the number: "))      
x=Solution()
print(x.subsetsum(a,b))