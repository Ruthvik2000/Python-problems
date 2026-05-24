class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=l+(r-l)//2
            check_if_halves_are_even=(r-mid)%2==0
            if nums[mid+1]==nums[mid]:
                if check_if_halves_are_even:
                    l=mid+2
                else:
                    r=mid-1
            elif nums[mid-1]==nums[mid]:
                if check_if_halves_are_even:
                    r=mid-2
                else:
                    l=mid+1
            else:
                return nums[mid]
        return nums[l]
                
"""
Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
"""