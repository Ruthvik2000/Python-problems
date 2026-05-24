def sd(A):
    i=0
    while(i<len(A)):
        if A[i]!=A[A[i]-1]:
            A[A[i]-1],A[i]=A[i],A[A[i]-1]
        elif A[i]==i+1:
            i=i+1
        elif A[i]==A[A[i]-1]:
            i=i+1
    print(A)
    #sorted A will be [1, 2, 3, 1, 5, 3, 2, 8] 
    # indexes 3,5,6 we need to cocentrate to return duplicate and missing value
    m={}
    d={}
    for i in range(len(A)):
        if A[i]!=i+1:
            if i not in d:
                d[i]=A[i]
            if i not in m:
                m[i]=i+1 
    print(d)
    print(m)
    x=[]
    for i,j in d.items():
        x.append(j)
    print(x)
    y=[]
    for i,j in m.items():
        y.append(j)
    print(y)
    ans=dict(zip(x,y))
    print(ans)
a=[1,2,3,8,2,3,5,1]
print(sd(a)) 

"""
output:
[1, 2, 3, 1, 5, 3, 2, 8]
{3: 1, 5: 3, 6: 2}
{3: 4, 5: 6, 6: 7}
[1, 3, 2]
[4, 6, 7]
{1: 4, 2: 7, 3: 6}
"""