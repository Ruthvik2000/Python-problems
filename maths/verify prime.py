class Solution:
    def isPrime(self, A):
        if A==1:
            return 0
        if A>1:
            for i in range(2,int(A**0.5)+1):#because the condition is prime number should divides with 1 and itself 
                                #So,if it is divided with any number between 2 and n-1 return 0
                                #else true
                if(A%i)==0:
                    return 0
            return 1

"""
taken the range upto sqrt(n) because after that all the values will be cofactors from the begging
example n=11
2,3,4,5,6,7,8,9,10
now the square root of 11 is 3 
S0 if we check 11%2,11%3 then its not necessary to check with the factors of 2 till 11 they are 2,4,6,8,10
                       and also its not necessary to check with the factors of 3 till 11 they are 6,9
"""
