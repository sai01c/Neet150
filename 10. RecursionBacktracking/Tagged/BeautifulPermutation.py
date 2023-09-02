"""
https://leetcode.com/problems/beautiful-arrangement/
"""

class Solution:
    def countArrangement(self, n: int) -> int:
        visit = set()
        res = 0
        nums = []
        for i in range(1, n+1):
            nums.append(i)
            
        def backtrack(i):
            if i == n:
                nonlocal res
                res += 1
                return
            for j in range(len(nums)):
                val = nums[j]
                ind = i + 1
                if (val not in visit):
                    if (ind%val == 0 or val%ind ==0):
                        visit.add(val)
                        backtrack(i+1)
                        visit.remove(val)
        backtrack(0)
        return res
        