l=[1,2,3,4,5]
m=['one','two','three','four','five']
d={}
for i in range(len(l)):
    d[l[i]]=m[i]
print(d)

#or we can use zip function 

"""
l=[1,2,3,4,5]
m=['one','two','three','four','five']
d=dict(zip(l,m))
print(d)
"""

"""
output:
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}      
"""

fruits=["apples","mangoes","grapes","orange"]

color=["Red", "Yellow", "Green", "Orange"]

h={}

for i,j in zip(fruits,color):

    h[i]=j

print(h)

"""
output:
{'apples': 'Red', 'orange': 'Orange', 'grapes': 'Green', 'mangoes': 'Yellow'}
"""
