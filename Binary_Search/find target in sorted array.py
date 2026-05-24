from collections import Counter
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        c=Counter(nums)
        for i,v in c.items():
            if i==target:
                return True
        return False 
    
"""
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: trues
"""