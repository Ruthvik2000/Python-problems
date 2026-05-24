def mergs(a):
    if len(a)>1:
        mid=len(a)//2
        L=a[:mid]
        R=a[mid:]
        mergs(L)
        mergs(R)
        i=0#points to left array
        j=0#points too right array
        k=0#points to the parent array
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                a[k]=L[i]
                i=i+1 
                k=k+1
            else:
                a[k]=R[j]
                j=j+1
                k=k+1
         # Checking if any element was left
        while i<len(L):
            a[k]=L[i]
            i=i+1 
            k=k+1
        while j<len(R):
            a[k]=R[j]
            j=j+1 
            k=k+1 
    return a
z=[1,5,8,9,23,6]
print(mergs(z))