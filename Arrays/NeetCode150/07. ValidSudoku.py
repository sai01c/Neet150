"""
https://leetcode.com/problems/valid-sudoku/


`collections.deafultdict(set)` this is a dictionary with set functionality. values are unique.  
Example: defaultdict(<class 'set'>, {0: {'5', '7', '3'}, 1: {'5', '9', '1', '6'}, 2: {'9', '8', '6'}})
this is discussed in DSA repo

we'll be maintaining defaultdict(set) for every row and column and also square. 
square we can get by //3
TC: O(n^2) if problem is matrix min is n^2
SC: O(n)
"""

import collections


def validSudoku(board):

    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9): #sudoku is always expected to be length 9
        for c in range(9):

            if board[r][c] == ".": #skip this case
                continue

            if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                return False #already existing so false

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])

    return True
