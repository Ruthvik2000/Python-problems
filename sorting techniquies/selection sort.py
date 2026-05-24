def selection(a):
    for i in range(len(a)-1):
        mini=i
        for j in range(i+1,len(a)):
            if a[j]<a[mini]:
                mini=j 
        if mini!=i:
            a[mini],a[i]=a[i],a[mini]
    return a
            
b=[-2,45,0,11,-9]
print(selection(b))

"""
output:
[-9, -2, 0, 11, 45]
"""