"""
https://leetcode.com/problems/shuffle-the-array/

Solution: this is very straight forward. First, have two pointer's - left and right. 
Now, iterate through them until left reached mid and right reached end. 
Create an empty array and append the values to it. 

Tc: O(n/2) 
Sc: O(nums)

"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n 
        res = []
        while left < n and right < len(nums):
            res.append(nums[left])
            res.append(nums[right])
            left+= 1
            right += 1
            
        return res
        