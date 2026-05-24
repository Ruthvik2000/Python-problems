s=str(input("enter the rooman string:"))
if len(s)>15 and len(s)<1:
    print("not valid")
dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
total=0
left=0#the previous digit
current=0#the current digit
for i in range(len(s)):
    current=dic[s[i]]#intialy taking the current as the first value of the given string
    if current > left:
        total=total+current-2*left#IV is the s then 1+5-2*1=4
    else:
        total=total+current
    left=current#to track the prev roman in every iteration we make prev = current
    """
    Its like IXV
    when the iteration completes till IX to track the I after itrating with X and V we use left=current
    """
print(total)
"""
    we subtract with 2 Because we are first adding that number, to subtract it we have to subtract it twice(to nullify                     the previous addition)
""" 

