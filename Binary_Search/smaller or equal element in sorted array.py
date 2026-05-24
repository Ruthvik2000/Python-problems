class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B==max(A):
            return len(A)
        l= 0
        r=len(A)-1
        ans=0
        while l<=r:
            mid=(l+r)//2
            if A[mid]>B:
                r= mid-1
            else:         #here we are taking both conditions equals to target and less than target
                ans=mid+1 #as we need to retrun the count we are adding 1
                l=mid+1
        return ans

"""
Input 1:
 A = [1, 3, 4, 4, 6]
 B = 4

 Output 1:
 4

Input 2:
 A = [1, 2, 5, 5]
 B = 3

 Output 2:
 2
"""