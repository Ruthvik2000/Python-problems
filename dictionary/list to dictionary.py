k=[1,2,3,5,6,6,7]#we given 6 as a duplicate after creating the dict it will remove the duplicates
d={}
for i in k:
    d.update({i:""})
print(d)

"""
output:
{1: '', 2: '', 3: '', 5: '', 6: '', 7: ''}
"""


"""
But if we assign the values the it wont remove the duplicates it just add into the list
k=[1,2,3,1,2,3]
d={}
for i in range(len(k)):
    d.update({i:k[i]})
print(d)

"""
output:
{0: 1, 1: 2, 2: 3, 3: 1, 4: 2, 5: 3}
"""
"""