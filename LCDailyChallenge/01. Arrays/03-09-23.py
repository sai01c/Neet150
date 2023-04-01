
"""
https://leetcode.com/problems/can-place-flowers/

Approach: if num is 0, if left of it and right of it are zero then we add 1.
we might also need to check boundaries. 
"""

def canPlaceFlowers(nums, n):
    m = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            continue
        if (i-1 < 0 or nums[i-1] == 0 and
        i+1 == len(nums) or nums[i+1] == 0):
            nums[i] = 1
            m += 1
    return m >= n


