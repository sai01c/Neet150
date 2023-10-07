"""
https://leetcode.com/problems/add-bold-tag-in-string/

"""

class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.intervals = []
    
    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.end = True
        
    def mergeIntervals(self, left, right):
        if not self.intervals:
            self.intervals.append([left, right])
        elif self.intervals[-1][1] < left:
            self.intervals.append([left,right])
        else:
            self.intervals[-1][1] = max(self.intervals[-1][1], right)
        
    def addBoldTag(self, s: str, words: List[str]) -> str:
        for word in words:
            self.addWord(word)
        
        for i in range(len(s)):
            curr = self.root
            lastIdx = None
            
            for j in range(i, len(s)):
                char = s[j]
                if char not in curr.child:
                    break
                curr = curr.child[char]
                if curr.end:
                    lastIdx = j + 1
            if lastIdx:
                self.mergeIntervals(i, lastIdx)
        
        res = ""
        prevEnd = 0
        for start, e in self.intervals:
            res += (s[prevEnd:start])
            res += "<b>"
            res += s[start:e]
            res += "</b>"
            prevEnd = e
        
        res += s[prevEnd:]
        
        return res
        
        