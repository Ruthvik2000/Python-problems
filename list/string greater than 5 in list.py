x=[a for a in input().split()]
print(x)
b=[]
c=[]
for i in x:
    if(len(i)>5):
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)