import sys  
class Solution:
    def minScoreTriangulation(self, values]):
        @lru_cache(maxsize=None) #@functools.cache
        def triangulation(start,end):
            if start+1==end:
                return 0
            minans=float('inf')
            for k in range(start+1,end):
                minans=min(minans,values[start]*values[k]*values[end]+triangulation(start,k)+triangulation(k,end))
            return minans        
        return triangulation(0,len(A)-1) 

"""

Input: values = [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
"""