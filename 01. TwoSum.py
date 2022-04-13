"""
https://leetcode.com/problems/two-sum/

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

EXPLANATION: Approach is to store the index, value of the array in a dicitionary. 
Iterate through the array and check the difference is in dictionary. 
If the difference is in dictionary, return that particular index and the iteration index. 

TC: we are iterating only once so it is O(n)
SC: we are using a dictionary so it is O(n)

"""


def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        seen[nums[i]] = i


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
