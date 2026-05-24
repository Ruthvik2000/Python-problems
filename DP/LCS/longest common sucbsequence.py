import sys
sys.setrecursionlimit(10**9)
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def helper(self,A,n,B,m):
        if n==0 or m==0:
            return 0 
        if (n,m) in self.d:
            return self.d[(n,m)]
        if A[n-1]==B[m-1]:
            self.d[(n,m)]=self.helper(A,n-1,B,m-1)+1
            return self.d[(n,m)]
        else:
            self.d[(n,m)]=max(self.helper(A,n,B,m-1),self.helper(A,n-1,B,m))
            return self.d[(n,m)]
        return self.d[(n,m)]
    def solve(self, A, B):
        if not A or not B:
            return 0
        self.d={}
        return self.helper(A,len(A),B,len(B))
        
"""
Example Input
Input 1:

 A = "abbcdgf"
 B = "bbadcgf"


Example Output
Output 1:

 5


Example Explanation
Explanation 1:

 The longest common subsequence is "bbcgf", which has a length of 5
"""


#tabulation
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        matrix = [ [ 0 for i in range(len(A)+1) ] for j in range(len(B)+1) ]  #Intialization
        for i in range(1,len(A)+1):
            for j in range(1, len(B)+1):
                if(A[i-1]==B[j-1]):
                    matrix[j][i] = matrix[j-1][i-1]+1
                else:
                    matrix[j][i] = max(matrix[j-1][i],matrix[j][i-1])
        # print(matrix)
        return matrix[len(B)][len(A)]