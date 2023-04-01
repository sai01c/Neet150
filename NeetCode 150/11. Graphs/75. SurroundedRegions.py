"""
https://leetcode.com/problems/surrounded-regions/

APPROACH: first, we iterate through the 4 boundaries and check for O and we extend 
based on dfs. These we cannot capture so we mark them as T

Now, we iterate and check for any O (we can capture them) so mark them as X
Next, iterate and check for T, we can bring them back to O as we cannot capture them

TC: O(m*n)
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visit = set()
        
        #we iterate over O cells and mark all the not capturable cells as T. if we are able to
        # reach other 0 from these boundary 0 then that means they are not capturable
        def dfs(r, c):
            if (r not in range(rows) or
               c not in range(cols) or 
               (r, c) in visit or
               board[r][c] != "O"):
                return
            
            board[r][c] = "T"
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)
        
        #we iterate over the boundaries and check for O and do dfs on them
        #after dfs on these cells, we mark them as T. all these cells can't be captured because they 
        #can be reached from boundary O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                    dfs(r, c)
                    
        #mark all cells that can be captured as X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        #these cells can not be captured so change them back to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"