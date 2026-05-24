ids = ['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
y=sorted(ids,key=lambda x:int(x[2:]))
print(y) 

"""
['id1', 'id2', 'id3', 'id22', 'id30', 'id100']

"""

#For desending order 
ids = ['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
ids.sort(key=lambda x:int(x[2:]),reverse=True)
print(ids)

"""
['id100', 'id30', 'id22', 'id3', 'id2', 'id1']
"""

"""
Both sort and sorted have three keyword arguments: cmp , key and reverse . 
Using key and reverse is preferred, because they work much faster than an equivalent cmp .
 key should be a function which takes an item and returns a value to compare and sort by.
  reverse allows to reverse sort order
"""
