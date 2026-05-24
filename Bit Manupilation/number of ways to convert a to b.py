def convert(a,b):
    x=a^b
    print(x)
    y=bin(x)[2:]
    print(y.count("1"))
convert(146,137)

"""
output:
27
4
"""
# x=146^137=27 
#then we will XOR where 1^0=1 and 0^1=1 So,the equal bits will return 0 using xor and the other will return 1 ,and that count of 1 is the number of ways to convert a to b