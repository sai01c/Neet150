"""
https://leetcode.com/problems/n-queens-ii/

tc - n!
"""
class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        res = 0
        sub = []
        for r in range(n):
            temp = []
            for c in range(n):
                temp.append(".")
            sub.append(temp)
        cols = set()
        pd = set()
        nd = set()
        
        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return
            for c in range(n):
                if (
                c in cols or
                (r+c) in pd or
                (r-c) in nd):
                    continue
                cols.add(c)
                pd.add(r+c)
                nd.add(r-c)
                sub[r][c] = "Q"
                backtrack(r+1)
                cols.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
                sub[r][c] = "."
        backtrack(0)
        return (res)
                
                