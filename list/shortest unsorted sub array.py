class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        for s in range(len(nums)-1):#slet s is the starting pointer
            if nums[s]>nums[s+1]:
                break
        for e in range(len(nums)-1,0,-1):#e is the ending pointer
            if nums[e]<nums[e-1]:
                break
        else:
            return 0
        mini=min(nums[s:e+1])
        maxi=max(nums[s:e+1])
        for i in range(s):
            if nums[i]>mini:
                s = i
                break
        for i in range(len(nums)-1, e, -1):
            if nums[i]<maxi:
                e = i
                break
        return e-s+1
