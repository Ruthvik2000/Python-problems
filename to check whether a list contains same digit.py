x=[int(a) for a in input().split()]
if nums.count(nums[0])>1 and nums.count(nums[0])==len(nums):
    print("contains same digit through out the list:",nums[0])
else:
    print("different elemnts")

"""
output:
enter a list:10                                                                                                                               
[10]                                                                                                                                          
different elemnts                                                                                                                             
                  

enter a list:1 1 1 1                                                                                                                          
[1, 1, 1, 1]                                                                                                                                  
contains same digit through out the list: 1    
"""