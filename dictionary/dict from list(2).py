k=[1,1,1,2,2,3]
d={}
for i in range(len(k)):
    d[k[i]]=k.count(k[i])
print(d)

"""
outpu:
{1:3,2:2,3:1}
"""