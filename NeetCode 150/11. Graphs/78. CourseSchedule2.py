class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []
        cycle = set()
        visit = set()
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(course):

            if course in cycle:
                return False
            if course in visit:
                return True  # why
            cycle.add(course)
            for c in prereq[course]:
                if dfs(c) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return res
