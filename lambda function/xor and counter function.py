from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums) # save counter in hashmap
        res = sorted(counter, key=lambda x:counter[x]) #sorted ascending
        return res[0]