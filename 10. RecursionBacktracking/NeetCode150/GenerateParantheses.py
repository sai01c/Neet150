"""
https://leetcode.com/problems/generate-parentheses/

Approach: this is a backtracking problem. We'll have a base case and list out all the possible cases. 

tc - 2** 2n. 2n because for input n we will have 2n characters
sc - n + 2**2n
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(curr, l, r):
            if len(curr) == 2*n and l==r:
                res.append(curr)
                return
            if l > n or r> n or r > l:
                return
            if len(curr) > 2*n:
                return
            
            backtrack(curr+"(", l+1, r)
            backtrack(curr+")", l, r+1)
        
        backtrack("", 0, 0)
        return res