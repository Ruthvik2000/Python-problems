A=[int(j) for j in input().split()]
k=int(input("enter the size of the window:\n"))
maxe=0
h=[]
for i in range(len(A)-k+1):
    maxe=A[i]
    for j in range(k):
        if A[i+j]>maxe:
            maxe=A[i+j]
    h.append(maxe)
print(h)

"""
1 2 3 1 4 5 2 3 6
enter the size of the window:
3
[3, 3, 4, 5, 5, 5, 6]

"""