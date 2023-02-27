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
"""


class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True  # for all the children, even if one of
                            # the children is true then we are good here so first true condition
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
