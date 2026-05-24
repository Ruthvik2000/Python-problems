n=int(input())
b=[]
for i in range(1,n+1,2):
    b.append(i)
print(b)
"""
#if we wont append then the for loop will execute 
#for example
n=int(input())
for i in range(1,n+1,2):
    print(i)

output:
1
3
5
"""
"""
if we use append then 
output will be in list format:[1,3,5]
"""
"""
            (OR)
x=list(range(1,5,2))
print(X)
"""