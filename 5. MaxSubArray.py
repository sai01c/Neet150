"""

https://leetcode.com/problems/maximum-subarray/

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

we need to iterate through the array and add elements to find the subarray sum. 
only case the sum of the subarray can be decreasing is ihe sum goes negative, so if the sum is negative we make it 0.
"""
