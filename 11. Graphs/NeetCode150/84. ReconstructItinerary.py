"""
https://leetcode.com/problems/reconstruct-itinerary/

Approach - 

tc
sc

"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        dic = defaultdict(list)
        for s, e in tickets:
            dic[s].append(e)
        res = ["JFK"]
        
        def dfs(node):
            if len(res) == len(tickets) + 1: return True
            if node not in dic: return False
            
            temp = list(dic[node])
            for i, nei in enumerate(dic[node]):
                dic[node].pop(i)
                res.append(nei)
                if dfs(nei): return True
                
                dic[node].insert(i, nei)
                res.pop()
            return False
        
        dfs("JFK")
        return res
            
            