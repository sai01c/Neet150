"""
https://leetcode.com/problems/combinations/

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sub = []
        
        def backtrack(i):
            if len(sub) == k:
                res.append(sub.copy())
                return
            
            for j in range(i, n+1):
                sub.append(j)
                backtrack(j+1)
                sub.pop()

                
        backtrack(1)
        return res