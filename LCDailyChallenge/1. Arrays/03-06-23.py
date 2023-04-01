"""
https://leetcode.com/problems/kth-missing-positive-number/

approach: we iterate through the nums, if number not in set then we increase the k
now, if k is 0 we can return the number

Tc: O(n)
Sc: O(n)
"""

def func(nums):
    numset = set(nums)
    for i in range(1, 10000):
        if i not in numset:
            k -= 1
        if k == 0:
            return i
