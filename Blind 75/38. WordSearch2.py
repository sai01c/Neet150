"""
https://leetcode.com/problems/word-search-ii/

Approach: this is similar to word search 1 but here we have lot of words.
so, we first add all these words to TrieNode() and then run dfs

Tc: O(m*n* dfs). dfs - 4^ max(len(word) in words)
Sc: O(n)
"""

class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        
    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.end = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        visit = set()
        res = set() #to avoid duplicates
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        def dfs(r, c, curr, word):
            if (r not in range(rows) or 
            c not in range(cols) or 
            (r,c) in visit or 
            board[r][c] not in curr.child):
                return 
            
            visit.add((r, c))
            curr = curr.child[board[r][c]] #moving to next trienode
            word += board[r][c] #adding this char to our word
            if curr.end == True: #this word exists in our trienode
                res.add(word)
            
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, curr, word)    
            visit.remove((r,c)) #removing since same letter cell can't be used more than once

            
                
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)
            