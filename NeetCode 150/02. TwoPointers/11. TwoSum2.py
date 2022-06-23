"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Approach: Here, it is mentioned that numbers are in sorted order. 
So, we can have two pointers and increase/decrease the pointers based on target

Tc: O(n) iterating the nums once using while loop
Sc: O(1) only pointers
"""


def twoSum2(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left+1, right+1]
        elif sum < target:
            left += 1
        elif sum > target:
            right -= 1


print(twoSum2([2, 7, 11, 15], 9))
