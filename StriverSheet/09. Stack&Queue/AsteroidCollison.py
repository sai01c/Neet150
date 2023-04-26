"""
https://leetcode.com/problems/asteroid-collision/

approach - monotonic stack because we need to compare with previous elements

tc - n
sc - n
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a) #add all elements
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                #check if this current element is less than 0 prevous element > 0
                # [-1,-1,2] check this example on why we are adding 3 conditions above 
                #then just follow the given conditions
                if abs(stack[-1]) < stack[-2]:
                    stack.pop()
                elif abs(stack[-1]) == stack[-2]:
                    stack.pop()
                    stack.pop()
                elif abs(stack[-1]) > stack[-2]:
                    val = stack.pop()
                    stack.pop()
                    stack.append(val)
    
        return stack
