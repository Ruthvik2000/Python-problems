x=[int(a) for a in input("enter the numbers:").split()]
target=(int(input("enter the target value:")))
y=sorted(x)
print(y)
l=[]
for i in range(0,len(y)-1):
    for j in range(i+1,len(y)):
        if y[i]+y[j]==target:
            l.append(tuple(sorted([i,j])))
print(list(set(l)))
            
output:
"""
enter the numbers:2 7 5 4 5                                                                                                                   
enter the target value:9                                                                                                                      
[2, 4, 5, 5, 7]                                                                                                                               
[(1, 2), (1, 3), (0, 4)]                                                                                                                      
"""