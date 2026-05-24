class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = round(sqrt(c))   # used "round" in order to avoid float values
        
        while i <= j:
            if (i*i + j*j) == c:
                return True
            elif (i*i + j*j) > c:
                j -= 1
            elif (i*i + j*j) < c:
                i += 1
                
        return False 

"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
"""
