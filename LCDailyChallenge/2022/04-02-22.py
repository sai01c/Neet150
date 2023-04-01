"""
https://leetcode.com/problems/valid-palindrome-ii/

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

first define palindrome method- have two pointers left and right. 
check their values and move them correspondingly. 

now, same concept but also check for (l,r-1) and (l+1,r)
"""


def valid(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if palindrome(s, l, r-1) or palindrome(s, l+1, r) is True:
                return True
            else:
                return False
    return True


def palindrome(string, l, r):
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True


s = "abc"
print(valid(s))
s = "abca"
print(valid(s))
s = "aba"
print(valid(s))
