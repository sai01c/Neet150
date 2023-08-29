"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/


"""

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic = defaultdict(list)
        #dic[parent] = [(child, dist), (child, dist)]
        for i in range(len(manager)):
            if manager[i] == -1:
                dic[i].append((i, informTime[i]))
            else:
                dic[manager[i]].append((i, informTime[i]))
        if len(manager) == 1: return informTime[0]
        
        ans = float('-inf')
        q = deque()
        visit = set()
        q.append((headID, informTime[headID]))
        visit.add(headID)
        while q:
            for i in range(len(q)):
                node, curr = q.popleft()
                if node not in dic:
                    ans = max(curr, ans)
                for nei, neiDist in dic[node]:
                    if nei not in visit:
                        q.append((nei, curr+neiDist))
        return ans