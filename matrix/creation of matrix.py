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
        print(matrix[i][j],end=" ") #end makes to print all numbers in single line
    print() #to seperate the each row(i) 

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


"""