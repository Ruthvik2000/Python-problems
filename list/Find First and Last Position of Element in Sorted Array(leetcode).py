m=[int(a) for a in input("enter the elements:").split()]
n=sorted(m)
print(n)
target=int(input("enter the target value:"))
x=[]
for i in range(len(n)):
    if n[i]==target:
        x.append(i)
print(x)
        