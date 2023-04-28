"""
https://leetcode.com/problems/similar-string-groups/

Approach - this is connected components problem. Firguring that is the biggest task
connect strings based on the given condition that max differing count is 2
now among these connections, find connected components

tc
sc

"""

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        dic = defaultdict(list)

        def diff(str1, str2):
            count = 0
            for i, j in zip(str1, str2):
                if i!= j:
                    count += 1
            return count

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if diff(strs[i], strs[j]) <= 2:
                    dic[i].append(j)
                    dic[j].append(i)
        
        visit = set()
        res = 0
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in dic[node]:
                dfs(nei)
        
        for i in range(len(strs)):
            if i not in visit:
                dfs(i)
                res += 1
        
        return res
        

    
    
