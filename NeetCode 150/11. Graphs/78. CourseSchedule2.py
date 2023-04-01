"""
https://leetcode.com/problems/course-schedule-ii/

Approach - 

tc - 
sc - 
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit, cycle = set(), set()
        res = []
        dic = defaultdict(list)
        for c, p in prerequisites:
            dic[c].append(p)
        
        def dfs(course):
            if course in cycle: return False
            if course in visit: return True
            cycle.add(course)
            
            for nei in dic[course]:
                if not dfs(nei):
                    return False
                
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        
        return res