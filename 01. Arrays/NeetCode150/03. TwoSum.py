"""
https://leetcode.com/problems/two-sum/

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
