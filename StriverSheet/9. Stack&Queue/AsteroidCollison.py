"""
https://leetcode.com/problems/asteroid-collision/

approach - monotonic stack because we need to compare with previous elements

tc
sc
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
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
            
