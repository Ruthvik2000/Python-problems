class Solution:
    def rotate(self,A,k:int):
        k=k%len(A)
        l=0
        r=len(A)-1
        while l<r:
            A[r],A[l]=A[l],A[r]
            l=l+1
            r=r-1 
        l=0
        r=k-1
        while l<r:
            A[r],A[l]=A[l],A[r]
            l=l+1
            r=r-1
        l=k
        r=len(A)-1
        while l<r:
            A[r],A[l]=A[l],A[r]
            l=l+1
            r=r-1 
        return nums
a=Solution()
nums=[1,2,3,4,5,6,7]
k=3 
print(a.rotate(nums,k)) 

"""
output:
[5, 6, 7, 1, 2, 3, 4]
"""

"""
other method
"""
class Solution:
    def rotate(self,A,k:int):
        k =k % len(nums)
        A[:] = A[-k:] + A[:-k]