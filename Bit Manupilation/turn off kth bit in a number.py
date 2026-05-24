#k=1 means right most bit
# to clear the kth bit
#Clearing a bit means that if K-th bit is 1, then clear it to 0 and if it is 0 then leave it unchanged
def turnoffkthbit(n,k):
    if k<=0:
        return n
    return n&(~(1<<k-1)) ## this type of representation is bit masking


# Function to check if k'th bit is set for `n` or not
def isKthBitSet(n, k):
    return (n & (1 << (k - 1))) != 0 


#Funtion to turn on the kth bit
def turnon(k,n):
    if k<=0:
        return n 
    return n|(1<<k-1) 

