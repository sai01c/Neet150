"""
https://leetcode.com/problems/course-schedule-ii/

Approach - we do regualar course schedule where we check for cycle but we add two extra things - 
first is add visit set so we don't add repeated nodes to our topological sort
second is we maintain array to add topological sort

tc - O(n) as we visit every node once
sc - n
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit, cycle = set(), set()
        res = []
        dic = defaultdict(list)
        for c, p in prerequisites:
            dic[c].append(p)
        
        def dfs(course):
            if course in cycle: return False #cycle exists so false
            if course in visit: return True #this node is already visited we don't want to add again
            cycle.add(course)
            
            for nei in dic[course]:
                if not dfs(nei):
                    return False
                
            cycle.remove(course) #remove from cycle
            visit.add(course) #mark as visited
            res.append(course) #add to topological sort output
            return True
        
        for c in range(numCourses):
            if not dfs(c): return [] #if cycle exists then no topological sort
        
        return res