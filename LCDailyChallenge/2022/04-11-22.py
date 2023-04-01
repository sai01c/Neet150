"""
https://leetcode.com/problems/game-of-life/

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

there can be 4 scenario's- 

old new type
0   0   0
1   0   1
0   1   2
1   1   3

we need to address these 4 scenario's.
First, write a function to count the neighbours.
now apply this function to the memebers and based on condition change them to types. 
now iterate through the board and change the type's back to 0 and 1. 

"""


def lifegame(board):
    rows = len(board)
    cols = len(board[0])

    def neighbour(r, c):
        count = 0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if (i == r and j == c) or i < 0 or j < 0 or i == rows or j == cols:
                    continue
                if board[i][j] in [1, 3]:
                    count += 1
        return count

    # this is for counting the neibhours and assigning types
    for r in range(rows):
        for c in range(cols):
            nei = neighbour(r, c)
            if board[r][c] == 1:
                if nei in [2, 3]:
                    board[r][c] = 3
            else:
                if nei == 3:
                    board[r][c] = 2
    print(board)
    # this is for assigning from type to new
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] in [2, 3]:
                board[r][c] = 1

    return board


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(lifegame(board))
