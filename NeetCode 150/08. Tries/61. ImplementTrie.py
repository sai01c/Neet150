"""
https://leetcode.com/problems/implement-trie-prefix-tree/

APPROACH: 
every time, we create a TrieNode which has dic and bool
first, we use dictionary to check if the char is in the node
we need to create a seperate TrieNode to initiate nodes
we also use endOfword to mark the end of word- will be used for search and startswith

TC: TODO
SC: TODO
"""

class TrieNode(): #idea of creating TrieNode with dic and bool is the key here
    def __init__(self):
        self.child = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:  # iterate through the word and add characters
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]

        curr.endOfWord = True  # mark last char as end of word

    def search(self, word: str) -> bool:

        curr = self.root
        for char in word:  # iterate through the word and try to eliminate if there's no char match
            if char not in curr.child:
                return False
            curr = curr.child[char]
        return curr.endOfWord  # if true means word has ended and search is true

    def startsWith(self, prefix: str) -> bool:

        curr = self.root
        for char in prefix:  # iterate through the word and try to eliminate if there's no char match
            if char not in curr.child:
                return False
            curr = curr.child[char]
        return True  # we just want starts with so its just True
