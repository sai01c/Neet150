"""
https://leetcode.com/problems/rearrange-array-elements-by-sign/

Approach- create two arrays with pos and neg elements.
join elements from them in alternate iteration to complete result array

tc - O(n)
sc - O(n) #array
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        p = 0
        n = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i]) #append to our two arrays - positive and negative
            else:
                neg.append(nums[i])
        res = []
        for i in range(len(nums)):
            if i % 2 == 0: #get elements from those arrays based on the index
                res.append(pos[p])
                p += 1 #increment the pointer's of these arrays
            else:
                res.append(neg[n])
                n += 1
        
        return res
    
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        p = 0
        n = 1
        for num in nums:
            if num > 0:
                res[p] = num
                p += 2    
            else:
                res[n] = num
                n += 2
        return res