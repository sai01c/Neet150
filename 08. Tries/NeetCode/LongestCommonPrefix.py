"""
https://leetcode.com/problems/longest-common-prefix/

"""

class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.end = True
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for word in strs:
            self.addWord(word)
        res = ''
        curr = self.root
        while curr and len(curr.child) == 1 and curr.end != True:
            for char in curr.child:
                res += char
                curr = curr.child[char]
        return res
        
        
        
        
        