"""
https://leetcode.com/problems/product-of-array-except-self/

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Approach is to iterate through the array from start and then iterate through the array from end.
[1,2,3,4] after first iteration [1,1,2,6] after second iteration [24,12,8,6]

TC: O(n) we are iterating through the loop
SC: O(n) we are creating an array 
"""


def product(nums):
    res = []
    p = 1
    for i in range(len(nums)):
        res.append(p)
        p *= nums[i]

    p = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= p
        p *= nums[i]
    return res
