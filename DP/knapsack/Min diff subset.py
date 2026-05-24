class Solution:
    # @param A : list of integers
    # @return an integer
    def subset(self,N,arr,s): #top_down
        dp = [[False for j in range(s+1)] for i in range(N+1)]
        for i in range(N+1):
            dp[i][0] = True 
        for i in range(1,N+1):
            for j in range(1,s+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N]
        
    def solve(self, A):
        # code here 
        n=len(A)
        rangee = sum(A)
        lastrow = self.subset(n,A,rangee)
        diff =0
        for j in range(rangee // 2,-1,-1):
            if lastrow[j] == True:
                diff = rangee - (2 * j)
                break
        return diff    

"""
Example Input
Input 1:

 A = [1, 6, 11, 5]


Example Output
Output 1:

 1


Example Explanation
Explanation 1:

 Subset1 = {1, 5, 6}, sum of Subset1 = 12
 Subset2 = {11}, sum of Subset2 = 11

"""