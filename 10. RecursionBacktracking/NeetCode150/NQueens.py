"""
https://leetcode.com/problems/n-queens/

Approach - regular backtracing template. First we place the queen in each row and make the possible options for next row

tc - n**n
sc - n**2
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pq = set()
        nq = set()
        res = []
        board = []
        for r in range(n):
            row = []
            for c in range(n):
                row.append(".")
            board.append(row)
            
        def backtrack(r):
            if r >= n:
                copy = []
                for i in board:
                    temp = "".join(i)
                    copy.append(temp)
                res.append(copy)
                return
            
            for c in range(n):
                if (c in cols or
                    r+c in pq or
                    r-c in nq):
                    continue
                    
                board[r][c] = "Q"
                cols.add(c)
                pq.add(r+c)
                nq.add(r-c)

                backtrack(r+1)

                cols.remove(c)
                pq.remove(r+c)
                nq.remove(r-c)
                board[r][c] = "."
            
        backtrack(0)
        return res
        