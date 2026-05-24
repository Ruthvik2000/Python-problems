def sort(a,b):
    i=0
    j=0
    k=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            k.append(a[i])
            i+=1 
        else:
            k.append(b[j])
            j=j+1 
    while i<len(a):
        k.append(a[i])
        i=i+1 
    while i<len(b):
        k.append(b[j])
        j=j+1 
    return k 
a=[4,5,6]
b=[6,8,9]
z=sort(a,b)
print(z)