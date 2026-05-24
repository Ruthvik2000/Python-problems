class Solution:
    def bpeak(self,A):
        l=0
        r=len(A)-1
        if len(A)<3:
            return None
        while l<=r:
            mid=(l+r)//2
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            elif A[mid]>A[mid-1] and A[mid]<A[mid+1]:
                l=mid+1 
            elif A[mid]<A[mid-1] and A[mid]>A[mid+1]:
                r=mid-1
            else:
                return -1
    def rot(self,A):
        k=self.bpeak(A)
        z=A[k+1:]
        return len(z)
a=[4,5,6,7,8,3,2,1]
k=Solution()
print(k.bpeak(a))
print(k.rot(a))

"""
4
3
"""