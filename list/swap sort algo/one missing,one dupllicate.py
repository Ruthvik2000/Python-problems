def sd(A):
    for i in range(len(A)):
        if A[i]==i+1:
            pass
        elif A[i]!=A[A[i]-1]:
            A[A[i]-1],A[i]=A[i],A[A[i]-1]
    for i in range(len(A)):
        if A[i]!=i+1:
            return([A[i],i+1])
    
a=[3,1,2,5,3]
print(sd(a))

"""
output:
[3, 4]
"""
