"""
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

"""

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        res = -1
        def helper(num):
            total = 0
            while num:
                digit = num % 10
                num = num // 10
                total += digit
            return total
        
        for i in range(len(nums)):
            total = helper(nums[i])
            if total in dic:
                temp = dic[total] + nums[i]
                res = max(res, temp)
                if nums[i] > dic[total]:
                    dic[total] = nums[i]
            else:
                dic[total] = nums[i]
        return res