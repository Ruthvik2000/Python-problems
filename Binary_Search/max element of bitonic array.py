#it means it's the peakof the bitonic array
class Solution:
    def find_highest_number(self,A):
        l=0
        r = len(A) - 1
        if len(A) < 3:
            return None
        while l<=r:
            mid = (l + r)//2
            if A[mid-1]<A[mid] and A[mid + 1]> A[mid]:
                l=mid + 1
            elif A[mid - 1] > A[mid] and A[mid + 1] < A[mid]:
                r = mid - 1
            elif A[mid - 1] < A[mid] and A[mid + 1] < A[mid]:
                return mid
            else:
                return None
a=[1,2,3,4,5,2,0]
k=Solution()
print(k.find_highest_number(a))
"""
4

"""