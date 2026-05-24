class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        r = max(time) * totalTrips * 10 # This is the worst case answer possible for any case. Could use big values like 10^15 as well but they might slow the time down for smaller cases.
        l = 0
        ans = 0

        def check_status(expected_time: int) -> int:
            nonlocal ans
            count = 0
            for i in time:
                count += expected_time // i # Total trips with time expected_time should be integer part of expected_time // i
            if count < totalTrips:
                return 1 # Since number of trips are less then required, left moves to mid
            elif count >= totalTrips:
                ans = expected_time # stores the latest result. This is guaranteed to be the minimum possible answer.
                return -1 # Since number of trips are greater/equal to required, right moves to mid

        while l < r-1: # Till Binary Search can continue. 
            mid = (l + r) // 2 # mid is the current expected time.
            status = check_status(mid) # The return values 1/-1 in check_status function determines which pointer to move.
            if status == 1:
                l = mid
            else:
                r = mid
                
        return ans

"""
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
"""
"""
Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

"""

"""
https://leetcode.com/problems/minimum-time-to-complete-trips/discuss/1802433/Python-Solution-oror-Detailed-Article-on-Binary-Search-on-Answer
"""