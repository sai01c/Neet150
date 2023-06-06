"""
https://leetcode.com/problems/sum-of-matrix-after-queries/

"""

class Solution:
    def matrixSumQueries(self, n, queries) -> int:
        rows = set()
        cols = set()
        res = 0
            
        for i in range(len(queries)-1, -1, -1):
            typ, ind, val = queries[i]
            if typ == 0 and ind not in rows:
                rows.add(ind)
                res += (val * (n-len(cols)))
            elif typ == 1 and ind not in cols:
                cols.add(ind)
                res += (val * (n-len(rows)))
        
        return res