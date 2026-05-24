nums=[1,1,2,2,2,3]
x=list(set(nums))
print(x)
y=[]
d={}
for i in range(len(x)):
    y.append(nums.count(x[i]))
print(y)
d=dict(zip(x,y))
print(d)
l=list()
d