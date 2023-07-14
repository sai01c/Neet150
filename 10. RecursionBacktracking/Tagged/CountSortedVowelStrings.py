"""
https://leetcode.com/problems/count-sorted-vowel-strings/

"""

class Solution:
    def countVowelStrings(self, n: int) -> int:
        strs = ['a', 'e', 'i', 'o', 'u']
        res = 0
        
        def backtrack(curr):
            if len(curr) == n:
                nonlocal res
                res += 1
                return
            
            for s in strs:
                if curr:
                    if curr[-1] <= s:
                        backtrack(curr+s)
                else:
                    backtrack(curr+s)
        backtrack("")
        return res
            
                