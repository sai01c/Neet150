"""
https://leetcode.com/problems/minimum-time-to-complete-trips/

Approach: this is binary search example like koko eating bananas, capacity to ship packages.
we need to calculate time for each trip and calculate trips to ship all the elements.
we run binary search on our actual time from min to max and for each time, we 
check if we can make total trips

Tc: O(nlogn)
Sc: O(1)

"""

def minimumTime(nums, totalTrips):
    left = min(nums)
    right = max(nums) * totalTrips

    def canShip(mid):
        trips = 0
        for num in nums:
            trips += (mid//num) 

        return trips > totalTrips

    while left <= right:
        mid = (left+right) // 2
        if not canShip(mid):
            left = mid + 1
        else:
            right = mid - 1 #we need minimum

    return left
            


    