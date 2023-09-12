"""
https://leetcode.com/problems/snakes-and-ladders/
"""

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        rows = len(board)
        cols = len(board[0])
        q = collections.deque()
        visit = set()
        q.append((1, 0))
        visit.add(1)
        length = len(board)
        
        def helper(square):
            r = (square-1) // length
            c = (square-1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]
        
        while q:
            x, moves = q.popleft()
            if x == length * length:
                return moves
            for dx in range(1, 7):
                newX = x + dx
                r, c = helper(newX)
                if r in range(rows) and c in range(cols) and board[r][c] != -1:
                    newX = board[r][c]
                if newX not in visit:
                    q.append((newX, moves + 1))
                    visit.add(newX)
        
        return -1
        
        