"""
https://leetcode.com/problems/word-ladder/

Approach - this should be BFS because it is similar to rotten oranges, wall ladder, etc
where from one node we get all possible nodes and from them we continue to get all possible ones
we need how many steps here that is the reason BFS


Tc
Sc
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        #dic = {pattern: [word1, word2]}
        dic = defaultdict(list)
        #for given words add all possible pattern and append words to these pattern
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:] #this is the key logic to this problem
                dic[pattern].append(word)
        q = collections.deque()
        visit = set()
        
        q.append(beginWord)
        visit.add(beginWord)
        res = 1 #start with 1 
        
        #generic BFS
        while q:
            for i in range(len(q)): 
                word = q.popleft()
                if word == endWord: #we found the answer
                    return res 
                #now, for the popped word, find all patterns and check for neighbours in our dic with this pattern
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in dic[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res += 1
            
        return 0 #that means no pattern exists
                    
