"""
https://leetcode.com/problems/valid-parentheses/

Approach: we create a dict with closing braces. 
while iterating throught the input, we check if it is an open or close brace - 
open brace we add to the stack. close brace we compare the last value in stack to the dict. 

TC: O(n) we are iterating once
Sc: O(n) stack

"""


def validParanthesis(input):
    dic = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = []
    for brace in stack:
        if brace not in dic:
            stack.append(brace)
        else:
            if stack and stack[-1] == dic[brace]:
                stack.pop()
            else:
                return False
    return True if not stack else False


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
