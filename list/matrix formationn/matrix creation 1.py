a=int(input("enter the number of rows"))
b=int(input("enter the number of coloums"))
matrix=[]
for i in range(a):
    m1=[]
    for j in range(b):
        m1.append(int(input("enter the num "+" "+str(i)+" "+str(j)+" ")))
    matrix.append(m1) 
for i in range(a): #if we want to show in matrix way then we want to again need to be read the values
    for j in range(b):
        print(matrix[i][j],end=" ")
    print()                 #this print statements is used to differentiate each i iterations


"""

enter the number of rows3
enter the number of coloums3
enter the num  0 0 1
enter the num  0 1 2
enter the num  0 2 3
enter the num  1 0 4
enter the num  1 1 5
enter the num  1 2 6
enter the num  2 0 7
enter the num  2 1 8
enter the num  2 2 9
1 2 3 
4 5 6 
7 8 9 


"""
