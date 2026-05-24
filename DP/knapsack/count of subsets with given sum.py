#python code using memization
class Solution:
    def __init__(self):
        self.d={}
    
    def helper(self,A,B,n):
        if B==0:
            return 1
        if n==0:
            return 0
        if (n,B) in self.d:
            return self.d[(n,B)]
        if A[n-1]>B:
            self.d[(n,B)]=self.helper(A,B,n-1)
            return self.d[(n,B)]
        if A[n-1]<=B:
            self.d[(n,B)]=self.helper(A,B-A[n-1],n-1)+self.helper(A,B,n-1)
        return self.d[(n,B)]    
    def subsetsum(self,A,B):
        n=len(A)
        return self.helper(A,B,n)
a=[int(a) for a in input().split()]
b=int(input("entre the number: "))      
x=Solution()
print(x.subsetsum(a,b)) 

"""
2 3 5 6 8 10
entre the number: 10
3
they are (2,3,5) (2,8) (10)
"""