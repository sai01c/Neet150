"""
https://leetcode.com/problems/valid-parentheses/

Approach: we shall create a dict with close ones as key. 
we iterate thorough the input and if we get open ones we append to stack 
if we get close ones we check if dict = stack and pop them 
if dict is not equal to stack return false
if stack is empty return true
if stack is not empty return false

Tc: O(n) we are iterating over them once
Sc: O(n) we are using count dictionary

"""


def isValid(s: str) -> bool:
    stack = []
    closeDict = {  # first create a dict with close one as key
        ")": "(",
        "}": "{",
        "]": "["
    }
    for char in s:
        if char in closeDict:  # if in dict means this is a close one
            # if equal we remove and proceed
            if stack and stack[-1] == closeDict[char]:
                stack.pop()
            else:
                return False  # they are not equal
        else:  # we add all the open one
            stack.append(char)
    return True if not stack else False  # we may have single bracket in stack
# if our stack is empty means we have popped everything and they all are equal.

