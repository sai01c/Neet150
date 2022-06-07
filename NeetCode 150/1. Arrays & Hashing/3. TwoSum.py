"""
https://leetcode.com/problems/two-sum/

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

EXPLANATION: Approach is to store the index, value of the array in a dicitionary. 
Iterate through the array and check the difference is in dictionary. 
If the difference is in dictionary, return that particular index and the iteration index. 

TC: we are iterating only once so it is O(n)
SC: we are using a dictionary so it is O(n)


"""


def twoSum(nums, target):
    seen = {}
    for index, val in enumerate(nums):
        remain = target - val
        if remain in seen:
            return seen[remain], index
        else:
            seen[val] = index


print(twoSum([2, 7, 11, 15], 9))
