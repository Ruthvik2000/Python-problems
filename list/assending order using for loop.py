x=[int(a) for a in input("enter the elements:\n").split()]
print(x)
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if(x[i] > x[j]):
           temp=x[i]
           x[i]=x[j]
           x[j]=temp
print("the asscending order",x)