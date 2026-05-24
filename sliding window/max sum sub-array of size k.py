class Solution:
    def maximumSumSubarray(k,arr):
        i=0
        j=0
        csum=0
        maxi=0
        while j<len(arr):
            csum=csum+arr[j]
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                maxi=max(maxi,csum)
                csum=csum-arr[i]
                i+=1
                j+=1
        return maxi
k=3
l=[1,2,3,5,4,8,9,10,3]
y=Solution()
print(y.maximumSumSubarray(k,l))

"""
output:
27
i.e 8,9,10
"""
