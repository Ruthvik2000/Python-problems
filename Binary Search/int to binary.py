class Solution:
	# @param A : integer
	# @return a strings
	def findDigitsInBinary(self, A):
        if A==0:
            return "0"
        n=A 
        ans=[]
        while(n>0):
            x=n%2
            ans.append(x)
            n=n//2 
        ans=ans[::-1]
        y="".join(map(str,ans))
        return y

"""
we can also do in one step
class Solution:
	# @param A : integer
	# @return a strings
	def findDigitsInBinary(self, A):
        if A==0:
            return "0"
        return bin(A)[2:]

"""