a=int(input("enter the number of rows"))
b=int(input("enter the number of coloums"))
m=[]
for i in range(a):
    c=[]
    for j in range(b):
        k=int(input("enter the numbers "+str(i)+" "+str(j)+" "))
        c.append(k)
    m.append(c)
    print()
print(m)
for i in range(a):
    for j in range(b):
        print(m[i][j],end=" ") 
    print()

print("After changinf the matrix")
for i in range(a):
    k=b-1
    for j in range(b):
        if i%2==0:
            print(m[i][j],end=" ")
        else:
            print(m[i][k],end=" ")
            k-=1 
    print() 

"""
enter the number of rows3
enter the number of coloums3
enter the numbers 0 0 1
enter the numbers 0 1 2
enter the numbers 0 2 3

enter the numbers 1 0 4
enter the numbers 1 1 5
enter the numbers 1 2 6

enter the numbers 2 0 7
enter the numbers 2 1 8
enter the numbers 2 2 9

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
1 2 3 
4 5 6 
7 8 9 
After changinf the matrix
1 2 3 
6 5 4 
7 8 9 
"""