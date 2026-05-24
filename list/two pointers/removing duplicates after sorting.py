class Solution:
    def removeDuplicates(self,A):
        j=1
        i=1
        A.sort()
        print(A)
        while i<len(A) and j<len(A):
            if A[i]!=A[i-1]:
                A[j]=A[i]
                i+=1
                j=j+1
            else:
                A.pop(i)
        return A
x=[1,2,4,3,45,5,5,3,5,3,3,3,3,3]
z=Solution()
print(z.removeDuplicates(x))

"""
output:
[1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 45]
[1, 2, 3, 4, 5, 45]
"""