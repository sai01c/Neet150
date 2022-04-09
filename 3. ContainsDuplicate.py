"""
https://leetcode.com/problems/contains-duplicate/submissions/

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false

EXPLANATION: 
1. First approach is to create a set of nums and compare the length of set and nums. 
2. Create a dictionary with frequency of the nums. Iterate over the values and check if value is more than 1.

TC: 
1. O(1) for len(set) and len(nums)
2. O(n) for iterating over the dictionary

SC:
1. O(n) for set
2. O(n) for dictionary
"""


from collections import Counter


def duplicate(nums):
    if len(set(nums)) < len(nums):
        return True
    return False


def duplicate1(nums):
    count = Counter(nums)
    for value in count.values():  # here we don't want to sort them by frequency.
        if value > 1:  # We just need to know if any of those has frequency of more than 1
            # so, we didn't copy the dict to a list. we iterate over the dict only.
            return True
    return False


print(duplicate1([1, 2, 3, 1]))
print(duplicate1([1, 2, 3, 4]))
