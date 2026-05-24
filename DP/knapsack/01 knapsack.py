import sys
sys.setrecursionlimit(10**9)
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def __init__(self):
        self.d={}
    def knapsack(self,wt,val,W,n):
        if n==0 or W==0:
            return 0
        if (n,W) in self.d:
            return self.d[(n,W)] 
        if wt[n-1]<=W:
            self.d[(n,W)]=max(val[n-1]+self.knapsack(wt,val,W-wt[n-1],n-1),self.knapsack(wt,val,W,n-1))
            return self.d[(n,W)]
        elif wt[n-1]>W:
            self.d[(n,W)]=self.knapsack(wt,val,W,n-1)
            return self.d[(n,W)]
    def solve(self, A, B, C):
        n=len(A)
        return self.knapsack(B,A,C,n) 

"""

"""
