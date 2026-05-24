class Solution:
    def ascending_search(self,A,l,r,B):
        while l<=r:
            mid=(l+r)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                l=mid+1 
            elif A[mid]>B:
                r=mid-1
        return -1
    def decsending_search(self,A,l,r,B):
        while l<=r:
            mid=(l+r)//2
            if A[mid]==B:
                return mid
            elif A[mid]<B:
                r=mid-1
            elif A[mid]>B:
                l=mid+1
        return -1
    def peak(self,A):
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
        return None
    def searchelement(self,A,B):
        p_index=self.peak(A)
        if A[p_index]==B:
            return p_index 
        a_index=self.ascending_search(A,0,p_index-1,B)
        d_index=self.decsending_search(A,p_index+1,len(A)-1,B)
        if a_index==-1 and d_index==-1:
            return -1
        if d_index!=-1:
            return d_index
        if a_index!=-1:
            return a_index
        
a=[1,2,3,4,5,1,0]
b=1
k=Solution()
print(k.peak(a))
print(k.searchelement(a,b))

"""
4
5

"""