a=input()
x=len(a)
print(x)
b=input()
c=int(input("enter at which position the second string need to be insert:"))
if c>x:
    print("insertion is not possible")
a=a[0:c]+b+a[c:]
print(a)
print("the position we enterd is:",c)
print(len(a))
"""
find=a.find(b)
print(b)
"""