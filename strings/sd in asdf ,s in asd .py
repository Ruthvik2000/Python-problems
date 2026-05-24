x=input()
y=x.split(" ")
print(y)
z=[]
for i in y:
    if(len(i)%2!=0):
        mid=len(i)//2
        z.append(i[mid])
    if(len(i)%2==0):
        mid=len(i)//2
        z.append(i[mid-1:mid+1])
print(z)

"""
asdf asd
['asdf', 'asd']
['sd', 's']
"""