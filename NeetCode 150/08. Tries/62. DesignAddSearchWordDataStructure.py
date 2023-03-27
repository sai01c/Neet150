"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/

APPROACH: 
adding is similar to adding into the trie data structure. 
but for searching, here there's a twist, we have . 
so, while iterating if there is no . then we can do the general search trie data strucure part. 
but, the tough part here is if there is .
essentially, what we want to do when there is . => 

for .ad example first iteration we start at . and 
then we start the recurisve dfs(i+1, child)
so now, first child here is b, cur will be at b. i is at 1 so char is "a"
now, a is there in cur.children (i.e. a and d)

this is a sexy problem, revise this many many times. 

TC: TODO
SC: TODO
"""

class TrieNode:
    def __init__(self):
        self.child = {}  # a : TrieNode
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(index, TrieNode):
            curr = TrieNode 
            #initiate the curr at this Trienode
            for i in range(index, len(word)):
                char = word[i]
                if char == ".": 
                    #we skip to next i value and next series of Trienodes
                    for children in curr.child.values(): #values because values are the trienodes
                        if dfs(i + 1, children):
                            return True
                    return False
                else: 
                    #regular Trienode case
                    if char not in curr.child:
                        return False
                    curr = curr.child[char]
            return curr.endOfWord
        
        return dfs(0, self.root) #running dfs on initial trienode
