"""
https://leetcode.com/problems/asteroid-collision/

Approach - this is a stack problem because we are comparing current element and removing based on given conditions


Tc
sc - O(n)
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
            