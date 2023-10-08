"""
https://www.geeksforgeeks.org/the-celebrity-problem/#

TODO
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for member in range(n):
            if knows(candidate, member):
                #celebrity should not know anyone so if we this returns True > our candidate can not be celebrity anymore
                candidate = member
            
        #we will get candidate where it does not know member
        for member in range(n):
            if (member != candidate) and (
                (
                    not knows(member, candidate)) or knows(candidate, member)
                ):
                return -1
        
        return candidate
                