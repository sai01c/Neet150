"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Approach: Before adding check if the current char == last value in stack. 
if yes remove it. if not just append it to the stack. this is greedy solution

Tc: O(n), Sc: O(n) stack
"""

def removeDuplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        
        else:
            stack.append(char)
    res = ""
    for char in stack:
        res += char
    return res

