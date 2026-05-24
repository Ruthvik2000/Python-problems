def xs(nums):
    for s in range(len(nums)-1):
        if nums[s]>nums[s+1]:
            break 
    return s 
a=[2,6,4,8,10,9,15]
print(xs(a)) 

"""
1
"""