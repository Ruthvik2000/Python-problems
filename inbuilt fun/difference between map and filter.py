def is_even(num):
    return num % 2 == 0


nums = [2, 4, 6, 7, 8]
filtered = filter(is_even, nums) 
print(*filtered) 

maped=map(is_even,nums)
print(*maped) 

"""
 filter(): formats new list that contains elements which satisfy specific condition.
 map(): function iterates through a all items in the given iterable and executes a function which we passed as an argument. 
 
""" 

"""
Note:
both Map and filter are ways of applying function to iterables. 
In Map you can use multiple iterables
whereas in filter only one iterable can be used
"""