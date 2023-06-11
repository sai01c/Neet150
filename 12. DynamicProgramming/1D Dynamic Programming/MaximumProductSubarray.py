"""
https://leetcode.com/problems/maximum-product-subarray/

approach: we need to keep track of every max and min because we might have negative numbers
so, [3,2,-2,-4] here if we take only positive - 6 but for all it is 48.
and, if number is 0 product may become 0, just intiate them to 1 again
don't know how this is dynamic programming - may be because we are storing every value

Tc: O(n)
Sc: O(1)
"""

def func(nums):
    minp, maxp = 1, 1
    res = nums[0]
    for num in nums:
        temp = maxp * num
        maxp = max(maxp*num, num, minp*num)
        minp = min(temp, num, minp*num)
        res = max(maxp, res)
    
    return res