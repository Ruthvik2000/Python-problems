x=[int(a) for a in input("enter the numbers:").split()]
print(x)
def fun(y):
    even=[]
    odd=[]
    for i in y:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)
fun(x)