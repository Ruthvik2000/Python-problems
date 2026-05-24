"""
Given an array of non negative integers A, and a range (B, C), 

find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C

Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]

where 0 <= i <= j < size(A)

Example :

A : [10, 5, 1, 0, 2]
(B, C) : (6, 8)
ans = 3 

as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]
"""
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def numRange(self, A, B, C):
		if B==0 and C==0:
			return 0
		sets=[]
		for i in range(len(A)):
			sum=0
			j=i
			while sum<B and j<len(A):
				sum+=A[j]
				j+=1
			while sum >= B and sum <= C and j <= len(A):
				if sum <= C:
					sets.append(A[i:j])
				if j<len(A):
					sum += A[j]
				j += 1
		return len(sets)