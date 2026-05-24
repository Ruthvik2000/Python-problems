x=""
y=input()
for i in range(len(y)): 
    if i%2==0: 
        x += y[i] 
print(x)
print(x[::-1])