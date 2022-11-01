"""
https://leetcode.com/problems/koko-eating-bananas/

Approach: Basically, in this problem, we have to find the minimum speed. So we consider the possible speeds 
i.e 1 to max of the given array. 
Now, we this is in increasing order so binary search
In the possible values, we calculate total time and then check for minimum speed. 

Tc: O(n logn) using for loop inside binary search
Sc: O(1)
"""


def func_piles(piles, h):
    left = 1 #start from 1? why?
    right = max(piles) #time complexity for this is still O(n)
    ans = float("infinity")
    while left <= right:
        mid = (left + right) // 2
        total_time = 0
        for p in piles:
            total_time += ((p-1) // mid) + 1
        if total_time <= h: #time is less than what we have, we can decrease speed to optimize
            ans = mid
            right = mid - 1
        else: #time is more than what we have, so increase speed
            left = mid + 1
    return ans


print(func_piles([3, 6, 7, 11], 8))
