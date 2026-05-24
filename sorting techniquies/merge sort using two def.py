def sort(a,b):
    i = 0
    j = 0
    ans = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
    if i == len(a):
        ans.extend(b[j:])
    else:
        ans.extend(a[i:])
    return ans

def merge_sort(A):
    if len(A) == 1:
        return A
    mid = len(A)//2
    l = merge_sort(A[:mid])
    r = merge_sort(A[mid:])
    return sort(l,r)

A = [18,1,2,5,6,87,9,5,4,1,2,365,8,9,78,54]
print(merge_sort(A))

"""
output:
[1, 1, 2, 2, 4, 5, 5, 6, 8, 9, 9, 18, 54, 78, 87, 365]

"""