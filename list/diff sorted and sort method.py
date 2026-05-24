l=[9,1,7,8,4,6,5,2,3]
l.sort()
print(l)
s_li=sorted(l)
print(s_li)
"""
output:
both will result the same output:
[1,2,3,4,5,6,7,8,9]

But for the diff is the sorted fun will return a new list
where as sort fun will sort the elements in the given list it self
"""
k=l.sort()
print(k)
"""
The output will be None  because the sort fun sort the elements to the given list itself
""" 