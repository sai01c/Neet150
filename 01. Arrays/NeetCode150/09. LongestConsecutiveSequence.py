"""
https://leetcode.com/problems/longest-consecutive-sequence/

Approach: first create a set of nums (only unique elements)
then, check if nums-1 is in set
now this is the current number and implement while loop to increaes the number by 1 and check if it is present in nums
if yes, increase the streak by 1

Tc: O(n)
Sc: O(n) using set
"""

def function1(nums):
    numSet = set(nums)
    max_streak = 0
    for num in nums:
        if num-1 not in numSet: #O(1) operation
            curr_num = num
            current_streak = 0
            while curr_num in numSet: #O(1) operation
                current_streak += 1
                curr_num += 1
            max_streak = max(current_streak, max_streak)
    return max_streak

