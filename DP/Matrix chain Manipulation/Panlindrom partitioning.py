import sys
sys.setrecursionlimit(10**9)
class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        if not A or A==A[::-1]:
            return 0
        cuts=float("inf")
        for k in range(1, len(A)):
            cuts=min(cuts,1+self.minCut(A[:k])+self.minCut(A[k:]))
        return cuts
