def First(arr,k):
    i=0
    j=0
    x=[] 
    y=[]#its the list need to be returned 
    while j<len(arr):
        if arr[j]<0:
            x.append(arr[j])
        elif arr[j]==x[0]:
            y.append(arr[j])   
        elif j-i+1<k:
            j+=1
        elif j-i+1==k:
            if not x:
                y.append(0)
            else:
                if(arr[j]==x[0]):
                    y.append(arr[j])
                    x.remove(x[0])
                    i+=1 
                    j+=1 
    return y
a=[12, -1, -7, 8, -15, 30, 16, 28]
b=3
print(First(a,b))
                    