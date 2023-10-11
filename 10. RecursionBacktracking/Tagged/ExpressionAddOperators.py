"""
https://leetcode.com/problems/expression-add-operators/

"""

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(i, prev, curr, value, s):
            if i == len(num):
                if value == target and curr == 0:
                    res.append(s)
                return
            
            curr = curr * 10 + int(num[i])
            if curr:
                backtrack(i+1, prev, curr, value, s)
            
            if not s:
                backtrack(i+1, curr, 0, value+curr, str(curr))
            else:
                backtrack(i+1, curr, 0, value + curr, s + "+" + str(curr))
                backtrack(i+1, -1*curr, 0, value - curr, s + "-" + str(curr))
                backtrack(i+1, prev * curr, 0, value-prev+prev*curr, s + '*' + str(curr))
        
        backtrack(0, 0, 0, 0, '')
        return res