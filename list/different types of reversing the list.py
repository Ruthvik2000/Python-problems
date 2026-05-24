#first method
x=[1,2,3]
print(x[::-1])


#second method
x=[1,2,3]
y=[]
for i in x[len(x)-1::-1]:
    y.append(i)
print(y)


#third method
x=[1,2,3]
y=[]
for i in reversed(range(len(x))):
    y.append(x[i])
print(y)

#fourth method
x=[1,2,3]
y=[]
for i in range(len(x)-1,-1,-1):
    y.append(x[i])
print(y)


"""
output:
[3,2,1]
"""

#in fourth method the middle -1 refers to the before index(last index of the list)of 
# the first index .So,that it prints upto first index


x=[1,2,3]
y=[]
for i in range(len(x)-1,-2,-1):
    y.append(x[i])
print(y)
#if we give the -2 instead of -1 then the output will be[3,2,1,3] ,because the for loops ends 
#iteration after printing the last index(-1) which will be next to the second last element x[-2]