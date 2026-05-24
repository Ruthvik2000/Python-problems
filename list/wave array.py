#So,the indexex need to be higher than the neighbours
def wave(A):
    for i in range(0,len(A),2):
        if (i<len(A)-1 and A[i]<A[i+1]):#In this condition when we at the first index it will check for that and all even indexes<len(A)-1
            A[i],A[i+1]=A[i+1],A[i]
        if (i>0 and A[i]<A[i-1]):#this condition check when we comes at the last index it will check for that and all even indexes>0
            A[i],A[i-1]=A[i-1],A[i] 
    return A 
a=[3,5,12,2,6,10,7,9,8]
print(wave(a))

"""
[5, 3, 12, 2, 10, 6, 9, 7, 8]
"""