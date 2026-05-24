class Solution:
    def matrixformation(self,a,b):
        matrix=[]
        for i in range(a):
            m1=[]
            for j in range(b):
                m1.append(int(input("enter the num "+" "+str(i)+" "+str(j)+" ")))
            matrix.append(m1)
        return matrix
    def summatrix(self,m1,m2):
        sume=[[0]*a]*b
        for i in range(a):
            for j in range(b):
                sume[i][j]=m1[i][j]+m2[i][j]
        return sume
a=int(input("enter the number of rows"))
b=int(input("enter the number of coloums"))
m1=Solution()
a1=m1.matrixformation(a,b)
print(a1)
m2=Solution()
a2=m2.matrixformation(a,b)
print(a2)
print(m1.summatrix(a1,a2)) #we can call summatrix fun using any object either m1 or m2 

"""
output:

enter the number of rows3
enter the number of coloums3
enter the num  0 0 1
enter the num  0 1 2
enter the num  0 2 3
enter the num  1 0 4
enter the num  1 1 5
enter the num  1 2 6
enter the num  2 0 7
enter the num  2 1 8
enter the num  2 2 9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
enter the num  0 0 9
enter the num  0 1 8
enter the num  0 2 7
enter the num  1 0 6
enter the num  1 1 5
enter the num  1 2 4
enter the num  2 0 3
enter the num  2 1 2
enter the num  2 2 1
[[9, 8, 7], [6, 5, 4], [3, 2, 1]]
[[10, 10, 10], [10, 10, 10], [10, 10, 10]]

"""