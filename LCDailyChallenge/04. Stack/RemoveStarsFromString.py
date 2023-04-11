"""
https://leetcode.com/problems/removing-stars-from-a-string/

Approach - very straightforward. we need to just know that we use stack.
we are using stack because we need to remove the previous element

tc O(n)
sc O(N)

"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
                
        return "".join(stack)
