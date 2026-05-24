a=int(input("Enter the number of rows:\n"))
b=int(input("enter the number of coloumns:\n"))
matrix=[]
for i in range(a):
    c=[]
    for j in range(b):
        k=input("enter the number "+str(i)+" "+str(j)+" ")
        c.append(k)
    print()
    matrix.append(c)
print(matrix)
for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=" ")
    print()
l=[]
for i in range(a):
    for j in range(b):
        if i<j:
            l.append(matrix[i][j])
#to shift the upper triangle elemenets to lower
k=0
for i in range(a):
    for j in range(b):
        if i>j:
            matrix[i][j]=l[k]
            k+=1 
print("Matrix after changing upper triangle elements to lower triangke")
for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=" ")
    print()

"""
Enter the number of rows:
3
enter the number of coloumns:
3
enter the number 0 0 1
enter the number 0 1 2
enter the number 0 2 3

enter the number 1 0 4
enter the number 1 1 5
enter the number 1 2 6

enter the number 2 0 7
enter the number 2 1 8
enter the number 2 2 9

[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
1 2 3 
4 5 6 
7 8 9 
Matrix after changing upper triangle elements to lower triangke
1 2 3 
2 5 6 
3 6 9 

"""