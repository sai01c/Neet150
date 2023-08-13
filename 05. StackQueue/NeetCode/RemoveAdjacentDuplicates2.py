
"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Approach: check if last index is same as char, then get the count of last index and add 1. now, if the 
count is == k, then pop k times. 
If the char is not equal append to stack and add count as 1.
"""

def removeDuplicates(s, k):
    stack = []
    for char in stack:
        if stack and stack[-1][0] == char:
            count = stack[-1][1]
            stack.append((char, count+1))
            if stack[-1][1] == k:
                for i in range(k):
                    stack.pop()
        else:
            stack.append((char, 1))
    res = ""
    for char, count in stack:
        res += char
    return res
    