class Solution:
    def findMin(self, A: List[int]) -> int:
        mine=A[0]
        l=0
        r=len(A)-1
        while l<=r:
            if A[l]<A[r]:       #condition for the unsorted array
                mine=min(mine,A[l])
                break
            mid=(l+r)//2 
            mine=min(mine,A[mid])
            if(A[mid]>=A[l]):
                l=mid+1 
            else:
                r=mid-1
        return mine

"""
other method
"""

class Solution:
    def findMin(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while l < r:
            mid = (l+r)//2
            if A[mid]>=A[l] and A[mid]>A[r]: #as we wanted to see the only right  part  we are taking l=mid+1
                l = mid + 1
            elif A[mid]<=A[l] and A[mid]<A[r]: #its not necessary for r=mid-1 beacause we are checking for nin element
                r = mid
            elif A[mid]>A[l] and A[mid]<A[r]:
                r=mid
        return A[l]
                
"""
Input: nums = [3,4,5,1,2]
Output: 1
"""