class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if mid>0 and mid<len(nums)-1:
                if nums[mid]>nums[mid-1] and nums[mid]> nums[mid+1]:
                    return mid
                elif nums[mid-1]> nums[mid]:
                    r=mid-1
                elif nums[mid+1]> nums[mid]:
                    l=mid+1
            elif mid==0:
                if nums[mid]>nums[mid+1]:
                    return 0
                else:
                    return 1
            elif mid==len(nums)-1:
                if nums[mid]>nums[mid-1]:
                    return len(nums)-1
                else:
                    return len(nums)-2

"""
Input: nums = [1,2,1,3,5,6,4]
Output: 5
"""