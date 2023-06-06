"""
https://leetcode.com/problems/sudoku-solver/

"""

from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        empty_cells = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])
                else:
                    empty_cells.append((r, c))
        
        def backtrack(cell_index):
            if cell_index == len(empty_cells):
                return True
            
            r, c = empty_cells[cell_index]
            square_index = (r // 3, c // 3)
            
            for i in range(1, 10):
                num = str(i)
                if num in rows[r] or num in cols[c] or num in squares[square_index]:
                    continue
                
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                squares[square_index].add(num)
                
                if backtrack(cell_index + 1):
                    return True
                
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                squares[square_index].remove(num)
            
            return False
        
        backtrack(0)
