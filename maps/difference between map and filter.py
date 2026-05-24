"""
map(): Applies a function to every item of an iterable.

filter(): Returns all elements of an iterable for which a function is true.
"""

#Multiplies each element by 2
 print(list(map(lambda x: x*2, [1,2,3,4])))

OUTPUT: [2, 4, 6, 8]

#Returns all elements greater than 2 
print(list(filter(lambda x: x>2, [1, 2, 3, 4])))

OUTPUT: [3, 4]  

print(list(map(lambda x: x>2, [1, 2, 3, 4]))) 

OUTPUT: [False, False, True, True]