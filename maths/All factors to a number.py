import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        if A==1:
            return [1]
        ans=[]
        for i in range(1,int(A**0.5)+1):
            if A%i==0 and i!=A**0.5:
                ans.append(i)
                ans.append(A//i)         
            if A%i==0 and i==A**0.5:
                ans.append(i)
        ans.sort()
        return ans

"""
if we take A=36 
sqrt of 36 is 6
where factors of 36 are:
1,2,3,4,6,9,12,18,36  

if we take number from front(let a) and last(let b) from the above row
(a,b)=(1,36)=(1,36//1)
(a,b)=(2,18)=(2,,36//2)
(a,b)=(3,12)=(3,36//3)
(a,b)=(4,9)=(4,36//4)
(a,b)=(6,6)=(6,36//6)
"""
"""
Its  enough to take the loop till int(A**0.5) 
and the 9,12,18,36 will be added to the ans list as ans.append(N//i)
"""