"""
https://leetcode.com/problems/course-schedule/

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Approach: first, create a dictionary with key as the course and value as the preRequisites for that course
{0: 1, 1: [2,3]}
Now, apply dfs for each course. For dfs we use a set and check if already visited
Next, iterate through all the courses and apply dfs on each course
"""

from ast import List


class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        preDic = {}
        for i in pre:
            if i[0] not in preDic:
                preDic[i[0]] = [i[1]]
            else:
                preDic[i[0]].append(i[1])

        visit = set()

        def dfs(course):
            if course in visit:  # cycle exists
                return False
            if course not in preDic:  # no prereq for this course
                return True
            # before checking for neighbors we need to add this to set to check for cycle
            visit.add(course)
            for nei in preDic[course]:
                if not dfs(nei):
                    return False
            visit.remove(course)
            preDic[course] = []
            return True

        # if numCourses is 2 that means courses are 0 and 1
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
