#memoization
class Solution:
    def __init__(self):
        self.d={}
    def helper(self,x,summ,n):
        if summ==0:
            return True
        if n==0:
            return False 
        if (n,summ) in self.d:
            return self.d[(n,summ)]
        if x[n-1]>summ:
            self.d[(n,summ)]=self.helper(x,summ,n-1)
            return self.d[(n,summ)]
        else:
            self.d[(n,summ)]=self.helper(x,summ-x[n-1],n-1) or self.helper(x,summ,n-1)
            return self.d[(n,summ)] 
        return d[(n,summ)]
    def equalsum(self,A):
        if sum(A)%2!=0:
            return False 
        if sum(A)%2==0:
            summ=sum(A)//2
            return self.helper(A,summ,len(A))
A=[int(a) for a in input().split()]
y=Solution()
print(y.equalsum(A)) 

"""
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""