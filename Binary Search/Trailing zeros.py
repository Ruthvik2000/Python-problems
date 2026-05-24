class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        a=str(bin(A))[2:][::-1]
        ind=a.index('1')
        return len(a[:ind]) 


######################OR##################

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        x=(bin(A))[2:]
        x=x[::-1] 
        if x.count('0')==len(x):
            return 0
        count=0
        for i in range(len(x)):
            if x[i]=='0':
                j=i+1
                while j<len(x):
                    count+=1 
                    if x[j]=='1':
                        break
                    j+=1
            break
        return count



"""
Explanation 1:

 18 in binary is represented as: 10010, there is 1 trailing zero.
Explanation 2:

 8 in binary is represented as: 1000, there are 3 trailing zeroes.
"""

"""
Example Input
Input 1:

 A = 18
Input 2:

 A = 8
"""

"""
Example Output
Output 1:

 1
Output 2:

 3
"""