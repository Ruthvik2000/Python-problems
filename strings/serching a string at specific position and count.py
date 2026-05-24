str=input()
x=input()
if (x in str):
    print("founded",x,"in the string")
count=str.count(x)
print(count)
count=str.count(x,7,10)
print(count)
find=str.find(x)
print(find)
find=str.find(x,7,13)
print(find)

"""
ruthvikhsdjg
h
founded h in the string
2
1
3
7
"""