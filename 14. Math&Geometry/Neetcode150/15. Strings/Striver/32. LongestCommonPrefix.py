class TrieNode:
    def __init__(self):
        self.dic = {}
        self.end = False
    
    def add(self, word):
        curr = self
        for char in word:
            if char not in curr.dic:
                curr.dic[char] = TrieNode()
            curr = curr.dic[char]
        curr.end = True
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()
        for word in strs:
            root.add(word)
        curr = root
        res =  ""
        while curr and len(curr.dic) == 1 and curr.end != True:
            for c in curr.dic:
                res += c
                curr = curr.dic[c]

        return res
            
        
        
        
        