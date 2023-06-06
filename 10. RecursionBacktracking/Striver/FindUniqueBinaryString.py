"""
https://leetcode.com/problems/find-unique-binary-string/

tc - 2**n 
sc - n
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        visit = set(nums)
        
        def backtrack(i, curr):
            if i >= n and curr not in visit:
                return curr
            if i >=n and curr in visit:
                return
            res = backtrack(i+1, curr+"1")
            if res: return res
            
            res = backtrack(i+1, curr+"0")
            if res: return res 
        
        return backtrack(0, "")