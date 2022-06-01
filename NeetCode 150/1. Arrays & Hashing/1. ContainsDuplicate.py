"""
https://leetcode.com/problems/contains-duplicate/submissions/

Approach: As this is a unique/duplicate problem, we can use set. Create a set of the given numbers
and then compare set and num to see any duplicates

Tc: O(n)
Sc: O(n)

Other Approach: this can be viewed as a frequency problem. 
Create a dict to get the frequency and check if it is greater than 1

Tc: O(n)
Sc: O(n)
"""


def duplicate(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for val in count.values():
        if val > 1:
            return True
    return False


def duplicateset(nums):
    nums_set = set(nums)
    if len(nums_set) != len(nums):
        return True
    return False


nums = [1, 2, 3, 4, 1]
print(duplicate(nums))
print(duplicateset(nums))
