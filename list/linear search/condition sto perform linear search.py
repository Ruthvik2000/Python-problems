pos=-1
def search(k,n):
    i=0
    while i<len(k):
        if k[i]==n:
            globals()['pos']=i
            return pos
        i=i+1
    else:
        return False
k=[2,3,4,6,8]
n=6
if search(k,n):
    print("Found at ",pos)
else:
    print("Not Found")
    
