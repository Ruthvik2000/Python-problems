def add(a,b):
  return a+b
A=[1,2,3,4,5]
B=[9,8,7,6]
# apply add() function to each item of the A,B list
add_numbers_iterator = list(map(add,A,B))
print(add_numbers_iterator)

"""
[10, 10, 10, 10] #map fun maped only 4 iterabols
"""



#using lambda in fun parameter 
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result)) 

"""
[9, 11, 13]
""" 


"""
Map() Function: 
The map() function iterates through all items in the given iterable and 
executes the function we passed as an argument on each of them.
 We can pass as many iterable objects as we want after passing the function we want to use.
""" 


"""
Filter() Function: Similar to map(), filter() takes a function object and an iterable and creates a new list.
 This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.
"""
