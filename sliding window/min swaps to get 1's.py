#Circular sliding window
"""
First, count the number of ones, say it is K.
Second, use a sliding window with length K.
"""
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cntOne = maxOne = 0
        l = r = 0
        n = len(data)
        while r < n*2:
            cntOne += data[r%n]
            r += 1
            while r - l > ones:
                cntOne -= data[l%n]
                l += 1
            maxOne = max(maxOne,cntOne)
        return ones - maxOne 

