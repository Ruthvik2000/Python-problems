class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
		#the list is not rotated: return the first element
        if nums[len(nums)-1] > nums[0]:
            return nums[0]
		#perform binary search 
        l, r = 0, len(nums)
        while l < r:
            mid= l + (r-l)//2
			# look for the transition point from maximum to minimum
            if mid== 0 or nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid
"""
input:[3,4,5,1,2]
output:1
"""