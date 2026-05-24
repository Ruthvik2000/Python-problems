def partition(a,low,high):
    pivot=a[low]
    start=low
    end=high
    while(start<end):
        while(a[start]<=pivot):
            start+=1
        while(a[end]>pivot):
            end-=1 
        if start<end:
            a[start],a[end]=a[end],a[start]
    a[end],a[low]=a[low],a[end]
    return end
def quickSort(a,low,high):
    if low<high:
        loc=partition(a,low,high)#taking the return value (end) of partion fun into the loc variable
        #it means loc value stores the pivot index
        quickSort(a,low,loc-1)
        quickSort(a,loc+1,high)
    return a
d=[8,7,2,1,0,9,6]
print(quickSort(d,0,len(d)-1))

"""
output:
[0, 1, 2, 6, 7, 8, 9]
"""