def Reverse(n):
    rev=0
    if n<0:
        x=n*-1
    elif n>0:
        x=n
    while(x>0):
        rem=x%10
        rev=rev*10+rem
        x=x//10
    if not rev in range(-2**31,2**31):
        return 0
    if(n>0):
        print(rev)
    elif(n<0):
        print(rev*-1)
n=int(input())
Reverse(n)