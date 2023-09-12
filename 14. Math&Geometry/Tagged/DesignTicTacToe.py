"""
https://leetcode.com/problems/design-tic-tac-toe/

instead of storing as lists, you can add +1 if player 1 and -1 if player 2 check if sum is +n or -n
"""

class TicTacToe:

    def __init__(self, n: int):
        self.rows = defaultdict(list)
        self.cols = defaultdict(list)
        self.pd = defaultdict(list)
        self.nd = defaultdict(list)
        self.n = n
        
    def move(self, r: int, c: int, player: int) -> int:
        self.rows[r].append(player)
        self.cols[c].append(player)
        self.pd[r+c].append(player)
        self.nd[r-c].append(player)
        
        if len(self.rows[r]) == self.n and len(set(self.rows[r])) == 1:
            return player
        if len(self.cols[c]) == self.n and len(set(self.cols[c])) == 1:
            return player
        if len(self.pd[r+c]) == self.n and len(set(self.pd[r+c])) == 1:
            return player
        if len(self.nd[r-c]) == self.n and len(set(self.nd[r-c])) == 1:
            return player
        
        return 0
        