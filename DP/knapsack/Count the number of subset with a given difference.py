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
    def subsetsum(self,A,diff):
        n=len(A)
        x=sum(A)
        reqSum=(diff+x)//2 #we need to find the count of subsets with sum==reqSum
        return self.helper(A,reqSum,n)
a=[int(a) for a in input().split()]
b=int(input("entre the difference number to be taken: "))      
x=Solution()
print(x.subsetsum(a,b)) 


"""
1 1 2 3
entre the difference number to be taken: 1
3
"""