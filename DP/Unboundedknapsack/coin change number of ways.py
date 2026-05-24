class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        d={}  
        def solve(i,amount): 
            if amount == 0: 
                return 1 
            if i<0 or amount<0: 
                return 0 
            if (i,amount) in d: 
                return d[(i, amount)] 
            if coins[i]<=amount: 
                d[(i, amount)] = solve(i,amount-coins[i]) + solve(i-1,amount)
            else: 
                d[(i, amount)] = solve(i-1,amount)
            return d[(i, amount)]
        return solve(len(coins)-1,amount) 

"""
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""
