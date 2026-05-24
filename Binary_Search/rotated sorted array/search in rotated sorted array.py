class Solution:
    def search(self, A: List[int], target: int) -> int:
        l=0
        r=len(A)-1
        while l<=r:
            mid=(l+r)//2
            if target==A[mid]:
                return mid 
            #left sorted portion
            if A[l]<=A[mid]:
                if target>A[mid] or target<A[l]:
                    l=mid+1 
                else:
                    r=mid-1 
            #right sorted array
            else:
                if target<A[mid] or target>A[r]:
                    r=mid-1 
                else:
                    l=mid+1 
        return -1
