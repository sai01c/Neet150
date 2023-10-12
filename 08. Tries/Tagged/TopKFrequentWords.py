"""
https://leetcode.com/problems/top-k-frequent-words/
"""

class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
    
    def addWord(self, curr, word):
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.end = True
    
    def traverseTrie(self, curr, prefix):
        res = []
        if curr.end:
            res.append(prefix)
        for charInd in range(26):
            char = chr((ord('a') + charInd)) 
            if char in curr.child:
                res += self.traverseTrie(curr.child[char], prefix + char)
        return res
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
            
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        freArr = []
        for i in range(len(words)+1):
            freArr.append(TrieNode())
        
        for word, fre in count.items():
            self.root.addWord(freArr[fre], word)
        
        res = []
        for i in range(len(freArr)-1, -1, -1):
            res += self.root.traverseTrie(freArr[i], "")
            if len(res) >= k:
                break
        return res[:k]
            
            
            
