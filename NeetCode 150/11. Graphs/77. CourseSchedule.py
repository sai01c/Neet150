"""
https://leetcode.com/problems/course-schedule/

Approach: first, create a dictionary with key as the course and value as the preRequisites for that course
{0: 1, 1: [2,3]}
Now, apply dfs for each course. For dfs we use a set and check if already visited
Next, iterate through all the courses and apply dfs on each course.

Tc: O() TODO
Sc: O(n) dic
"""

import collections

class Solution:
    def canFinish(self, numCourses: int, pre) -> bool:
        preDic = collections.defaultdict(list)
        for k, v in pre: #adding to the dictionary
            preDic[k].append(v)
        visit = set()

        def dfs(course):
            if course in visit:  # cycle exists
                return False
            if course not in preDic or preDic[course] == []:  
                # no prereq for this course
                return True
            # before checking for neighbors we need to add this to set to check for cycle
            visit.add(course)
            for nei in preDic[course]:
                if not dfs(nei):
                    return False
            visit.remove(course) #remove from cycle as this is already done
            preDic[course] = [] #this is for elimination TLE. 
            
            return True

        # if numCourses is 2 that means courses are 0 and 1
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
