#this quetion is same as count the number of subsets with given difference
class Solution:
    def __init__(self):
        self.d={}
    def helper(self,A,B,n):
        if B==0:
            return 1
        if n==0:
            return 0
        if (n,B) in self.d:
            return self.d[(n,B)]
        if A[n-1]>B:
            self.d[(n,B)]=self.helper(A,B,n-1)
            return self.d[(n,B)]
        if A[n-1]<=B:
            self.d[(n,B)]=self.helper(A,B-A[n-1],n-1)+self.helper(A,B,n-1)
        return self.d[(n,B)]    
    def subsetsum(self,A,diff):
        n=len(A)
        x=sum(A)
        reqSum=(diff+x)//2 #we need to find the count of subsets with sum==reqSum
        return self.helper(A,reqSum,n)
a=[int(a) for a in input().split()]
b=int(input("entre the target to be taken: "))      
x=Solution()
print(x.subsetsum(a,b))  


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arr_sum = 0
        arr_sum = sum(nums)
        target = abs(target)
        if (target>arr_sum or (arr_sum + target)%2 == 1):
            return 0
        
        return self.countSubset(nums,  (arr_sum + target)//2)
    def countSubset(self, arr, arr_sum):
        n = len(arr)
        dp = [[0 for i in range(int(arr_sum + 1))] for y in range(n + 1)]
        #Fill first col with true
        for i in range(n + 1):   
            dp[i][0] = 1
        # Fill the first row with sum as first index
        for j in range(1, arr_sum + 1):
            dp[0][j] = 0
        for i in range(1, n + 1):
            for s in range(0, int (arr_sum) + 1):
                dp[i][s] = dp[i - 1][s]
                if s>=arr[i - 1]:
                    dp[i][s] += dp[i - 1][s - arr[i -1]]

        return dp[n][arr_sum]
    

"""
1 1 1 1 1
entre the target to be taken: 3
5
"""
"""
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
"""