"""
https://leetcode.com/problems/word-search/

approach: we use dfs and add index to this dfs. We iterate in four directions and 
check for the next index if they are equal we proceed further

Tc: 
Sc: 

"""
def wordSearch(board, word):
    rows = len(board)
    cols = len(board[0])
    visit = set()
    directions = [[0,1], [0,-1], [1,0], [-1,0]]

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r not in range(rows) or
            c not in range(cols) or 
            (r,c) in visit or
            word[i] != board[r][c]):
            return False
        visit.add((r,c))
        for dr, dc in directions:
            nr, nc = r+dr, c+ dc
            if dfs(nr, nc, i+1):
                return True

        visit.remove((r,c))

    for r in rows:
        for c in cols:
            if dfs(r, c, 0):
                return True
    return False