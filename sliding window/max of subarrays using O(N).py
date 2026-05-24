class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = collections.deque()  #step 1
        
        for i ,num in enumerate(nums):  #step2
            
            while dq and num > nums[dq[-1]]: #step3
                dq.pop()
                
            dq.append(i) #step4
            
            if i-k == dq[0]: #step5
                dq.popleft()
                
            if i >= k-1: #step6
                ans.append(nums[dq[0]])
        return ans           
"""
1.create a deque and an ans list to strore the final ans
2.loop the the given input list
3.pop the deque from the right untill the rightmost element of the queue is greater than the current element in the loop (note that the deque is only storing the index)
4.insert the current elements index to the right of the deque
5.if the the leftmost element of the deque is equal to i-k then it is no loger under consideration so we pop it
6.for every cycle of the loop after the threshold i >=k-1 we push it to the ans list
"""

"""
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""