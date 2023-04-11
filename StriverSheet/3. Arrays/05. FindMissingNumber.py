"""
https://leetcode.com/problems/missing-number/

Approach - calculate sum using (n * (n+1 / 2)) then get the missing number

tc - O(n)
sc - O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        given = 0
        n = len(nums)
        total = (n * (n+1)) / 2 #get the total sum of numbers
        for num in nums:
            given += num #get the sum of given elements
        return int(total - given) #subtract to get the missing element
        