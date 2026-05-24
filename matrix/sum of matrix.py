def matrix(a,b,m):
    for i in range(a):
        c=[]
        for j in range(b):
            k=int(input("enter the numbers "+str(i)+" "+str(j)+" "))
            c.append(k)
        m.append(c)
        print()
    return m
a=int(input("enter the number of rows"+" "))
b=int(input("enter the number of coloums"+" "))

matrix1=[]
matrix(a,b,matrix1)
matrix2=[]
matrix(a,b,matrix2)
print(matrix1)
print(matrix2)

result = [[matrix1[i][j] + matrix2[i][j]  for j in range(b)] for i in range(a)]
#else we can create a n*m 0 matrix and append that
"""
summ =[[0]*b for j in range(a)]
for i in range(a):
    for j in range(b):
        summ[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range(a):
    for j in range(b):
        print(summ[i][j],end=" ")
    print()
"""
print(result)
for i in range(a):
    for j in range(b):
        print(result[i][j],end=" ")
    print() 


"""
enter the number of rows 2
enter the number of coloums 2
enter the numbers 0 0 1
enter the numbers 0 1 2

enter the numbers 1 0 3
enter the numbers 1 1 4

enter the numbers 0 0 1
enter the numbers 0 1 2

enter the numbers 1 0 3
enter the numbers 1 1 4

[[1, 2], [3, 4]]
[[1, 2], [3, 4]]
[[2, 4], [6, 8]]
2 4 
6 8 
"""