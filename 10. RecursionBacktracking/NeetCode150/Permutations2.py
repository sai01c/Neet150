"""
https://leetcode.com/problems/permutations-ii/

"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        count = Counter(nums)
        
        def backtrack():
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    sub.append(n)
                    count[n] -= 1
                    backtrack()
                    sub.pop()
                    count[n] += 1
        
        backtrack()
        return res