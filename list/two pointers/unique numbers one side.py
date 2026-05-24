class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self,A):
        A.sort()
        print(A)
        if len(A)==0: return 0
        if len(A)==1: return 1
        j = 1
        for i in range(1,len(A)):
            if(A[i]!=A[i-1]):
                A[j]=A[i]
                j+=1
        print(A)
        return j
x=[1,2,4,3,45,5,5,3,5,3,3,3,3,3]
z=Solution()
print(z.removeDuplicates(x))

"""
output:
[1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 45]
[1, 2, 3, 4, 5, 45, 3, 3, 3, 4, 5, 5, 5, 45]
6

"""
