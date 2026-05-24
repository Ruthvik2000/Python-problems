def buuble(n):
    for i in range(len(n)-1):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n
n=[5,4,6,2,8]
print(buuble(n))

"""
enter the elements;
10 25 15 60 45 30
[10, 25, 15, 60, 45, 30]
[10, 15, 25, 30, 45, 60]
"""

"""
As the first loop starts the iteration after the end of that iteration it fixes the highest number at the end 
it's like 10 15 25 45 30 60
In the second iteration of the outer loop the reslt after the second iteration will be
10 15 25 30 45 60
the third iteration of outer loop will be
10 15 25 30 45 60
In this way it executes 4,5
So to neglet the last position's of fixed highest numbers in  the list, we used inner loop iteration only len(n)-i-1
"""

#we can observe that len(n)-1 outer iterations is enough to get sorted list
#So,we took len(n)-1 in the outer loop execution
