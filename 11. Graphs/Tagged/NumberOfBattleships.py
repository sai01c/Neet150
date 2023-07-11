"""
https://leetcode.com/problems/battleships-in-a-board/

Microsoft
"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        visit = set()
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        
        def dfs(r, c):
            if (r not in range(rows) or
               c not in range(cols) or
               (r,c) in visit or
               board[r][c] != "X"):
                return
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and board[r][c] == "X":
                    dfs(r,c)
                    res += 1
        
        return res