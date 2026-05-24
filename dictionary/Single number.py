class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, nums):
        num_dict = {}
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            if nums[i] in num_dict:
                num_dict[nums[i]] += 1
            else:    
                num_dict[nums[i]] = 1
        
        for key in num_dict:
            if num_dict[key] == 1:
                return key

"""
Input 1:

 A = [1, 2, 2, 3, 1]

 output1:
 3
"""