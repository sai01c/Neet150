"""
https://www.lintcode.com/problem/892/

Approach: 

"""

def alienDictionary(words):
    dic = {}
    for word in words:
        for char in word:
            dic[char] = set()
    
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
            return ""
        for j in range(minLen):
            if w1[j] != w2[j]:
                dic[w1[j]].add(dic[w2[j]])
                break #why break the loop

    visit = {}
    res = []

    def dfs(char): #post order dfs
        if char in visit:
            return visit[char] #true - current path, false - visited
        
        visit[char] = True #current path
        for nei in dic[char]:
            if dfs(nei):
                return True
        visit[char] = False
        res.append(char)

    for char in dic:
        if dfs(char):
            return ""
    return res.reverse() #array