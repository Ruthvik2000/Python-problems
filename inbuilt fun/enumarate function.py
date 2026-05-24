"""
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
"""
#its like instead of creating a dictionary we will use this built-in-fun to create a tuple with counter to the all objects
# enumerate function in loops


l1 = ["eat","sleep","repeat"]
for i in enumerate(l1):
    print(i)


"""
output:
(0, 'eat')                                                                                                                                    
(1, 'sleep')                                                                                                                                  
(2, 'repeat') 
"""

# changing index and printing separately
l1 = ["eat","sleep","repeat"]
for index,value in enumerate(l1,100):
    print(index,value)

"""
output:

100 eat                                                                                                                                       
101 sleep                                                                                                                                     
102 repeat                                                                                                                                    
            
"""