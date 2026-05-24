"""
The reversed() function returns an iterator that accesses the given sequence in the reverse order.
after that we have converted the iterators returned by reversed() to list using the list() function.
"""

# for string
seq_string = 'Python'
print(list(reversed(seq_string)))

# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))

# for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))

# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list))) 

"""
['n', 'o', 'h', 't', 'y', 'P']
['n', 'o', 'h', 't', 'y', 'P']
[8, 7, 6, 5]
[5, 3, 4, 2, 1]
""" 

#The reverse() method doesn't return any value. It updates the existing list. 
x=[1,2,3,4]
x.reverse()
print(x) 

"""
[4,3,2,1]
""" 


#If you need to access individual elements of a list in the reverse order, it's better to use the reversed() function.

systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o) 

"""
Linux
macOS
Windows
"""