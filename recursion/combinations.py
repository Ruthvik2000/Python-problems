class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solu(n:int,k:int)->list[list]:
            if k==1: return [[i+1] for i in range(n)]
            if n==k: return [[i+1 for i in range(n)]]
            return solu(n-1,k)+[i+[n] for i in solu(n-1,k-1)]
        return solu(n,k)

"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 bg
"""