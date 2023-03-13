"""
https://leetcode.com/problems/maximum-subarray/

Pattern: Sliding window ( as we are moving through the array ), Kadane’s algorithm. 
we need to iterate through the array and add elements to find the subarray sum. 
only case the sum of the subarray can be decreasing is the sum goes negative, 
so if the sum is negative we make it 0.
Follow- up: Divide and conquer ??

TC: we are iterating only once so O(n)
Sc: O(1) no additional space is required. 
"""

def maxSum(nums):
    ans = nums[0]
    runSum = 0
    for num in nums:
        if runSum < 0:
            runSum = 0
        runSum += num
        ans = max(ans, runSum)
    return ans


print(maxSum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
