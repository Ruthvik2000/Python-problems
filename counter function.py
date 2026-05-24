from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']
x=Counter(list1)
print(x)
"""
output:
Counter({'x': 4, 'z': 2, 'y': 2})
"""

#Counter with Dictionary
from collections import Counter
dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
print(Counter(dict1))

"""
oytput:
Counter({'x': 4, 'y': 2, 'z': 2})
"""

#Counter with tuple
from collections import Counter
tuple1 = ('x','y','z','x','x','x','y','z')
print(Counter(tuple1))
"""
output:
Counter({'x': 4, 'y': 2, 'z': 2})
"""

  