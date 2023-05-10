"""
https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

Approach - this is again connected components problem. 
first you calculate total number of edges for given size of connected component
then find connected components each iteration and subtract number of edges from total

tc - O(n)
sc - O(n)

"""

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        dic = defaultdict(list)
        for s, e in edges:
            dic[s].append(e)
            dic[e].append(s)

        def dfs(node): #adding connected componenets to visit
            if node in visit: return
            visit.add(node)
            for conn in dic[node]:
                dfs(conn)
        
        prev = 0
        actual = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                temp = len(visit) #this is the length of visit array 
                curr = temp - prev #but this might contain previous iteration so just calculate this iteration
                actual += self.numberOfEdges(curr) #keep adding actual edges of our connected componnets
                prev = temp #update previous to this iteration
        
        total = self.numberOfEdges(n) #total number of edges for given n

        return total - actual
    
    def numberOfEdges(self, n): #function to calculate number of edges draw this on paper to obtain this relation
        if n == 1: return 0 
        return (self.numberOfEdges(n-1) + (n-1))