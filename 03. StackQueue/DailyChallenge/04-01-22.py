"""
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

have two pointers left, right and swap them 
increase and decrease pointers respectively
"""


def reverse(string):
    l = 0
    r = len(string) - 1
    while l < r:
        string[l], string[r] = string[r], string[l]
        l += 1
        r -= 1
    return string


s = ["H", "a", "n", "n", "a", "h"]
print(reverse(s))
s = ["h", "e", "l", "l", "o"]
print(reverse(s))


def reverseStack(string):
    stack = []
    i = 0
    for _ in string:
        stack.append(_)
    while stack:
        string[i] = stack.pop()
        i += 1
    return string


s = ["H", "a", "n", "n", "a", "h"]
print(reverseStack(s))
s = ["h", "e", "l", "l", "o"]
print(reverseStack(s))
