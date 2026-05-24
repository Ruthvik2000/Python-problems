class Solution:
    def Firstoccurence(self,A,B):
        l=0
        r=len(A)-1
        l_ele=-1
        while l<=r:
            mid=l+(r-l)//2
            if A[mid]==B:
                l_ele=mid#storing mid index in l_ele
                r=mid-1#to get the first occuring number we will move r pointer to mid-1
            elif A[mid]<B:
                l=mid+1 
            elif A[mid]>B:
                r=mid-1
        return l_ele
    def lastoccurence(self,A,B):
        l=0
        r=len(A)-1
        r_ele=-1
        while l<=r:
            mid=l+(r-l)//2
            if A[mid]==B:
                r_ele=mid#storing mid index in r_ele
                l=mid+1#to get the last occuring number we will move l pointer to mid+1
            elif A[mid]<B:
                l=mid+1 
            elif A[mid]>B:
                r=mid-1
        return r_ele
a=[2,4,10,10,10,18,20]
b=10
k=Solution()
print(k.Firstoccurence(a,b))
print(k.lastoccurence(a,b))


"""
2
4
"""