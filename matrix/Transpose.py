def matrix(a,b,m):
    for i in range(a):
        c=[]
        for j in range(b):
            k=int(input("enter the numbers "+str(i)+" "+str(j)+" "))
            c.append(k)
        print()
        m.append(c)
    return m
def transpose(m):
    t=[[m[j][i] for j in range(len(m))]for i in range(len(m[0]))]
    return t 
a=int(input("enter the number of rows "))
b=int(input("enter the number of coloumns"))
m=[]
mat1=matrix(a,b,m)
print(mat1)
for i in range(a):
    for j in range(b):
        print(mat1[i][j],end=" ")
    print()
mat2=transpose(mat1)
print(mat2)
for i in range(b):
    for j in range(a):
        print(mat2[i][j],end=" ")
    print() 

"""
enter the number of rows 2
enter the number of coloumns3
enter the numbers 0 0 1
enter the numbers 0 1 2
enter the numbers 0 2 3

enter the numbers 1 0 4
enter the numbers 1 1 5
enter the numbers 1 2 6

[[1, 2, 3], [4, 5, 6]]
1 2 3 
4 5 6 
[[1, 4], [2, 5], [3, 6]]
1 4 
2 5 
3 6 
"""
