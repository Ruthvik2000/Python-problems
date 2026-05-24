x=[]
for i in range(3):
    y=[int(a) for a in input("enter the number").split()]
    x.append(y)
print(x) 

"""
output:

enter the number1 2
enter the number3 4
enter the number5 6
[[1, 2], [3, 4], [5, 6]]
"""