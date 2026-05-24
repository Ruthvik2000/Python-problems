#the que is to find the min diff element when we subtract with B
class Solution:
    def mindiffelement(self,A,B):
        l=0
        r=len(A)-1
        while(l<=r):
            mid=(l+r)//2
            if A[mid]==B:
                return A[mid]
            elif A[mid]<B:
                l=mid+1 
            else:
                r=mid-1 
        if abs(A[r]-B)<abs(A[l]-B):
            return A[r]
        else:
            return A[l]
a=[1,3,8,10,15]
b=12
k=Solution()
print(k.mindiffelement(a,b))