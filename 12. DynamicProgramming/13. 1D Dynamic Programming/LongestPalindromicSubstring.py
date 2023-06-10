"""
https://leetcode.com/problems/longest-palindromic-substring/

Approach: this is a palindromic substrings question so approach is to start from the middle
and decrease the left and increase the right pointer

Tc: O(n) as we are iterating over the string once
Sc: O(n) as we are using res for storing the string

"""

def longpalinsubstr(s):
    res = ""
    for i in range(len(s)):
        odd = palindromeSubstring(s, i, i)  # if input length is odd
        if len(odd) > len(res):  # we want the max length substr so this
            res = odd
        even = palindromeSubstring(s, i, i+1)  # if input length is even
        if len(even) > len(res):
            res = even
    return res


def palindromeSubstring(s, left, right):
    # start from middle check palindrome and increase/decrease the pointers
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # actual should be s[left:right+1] but our pointers already moved so adjust
    return s[left+1: right]


print(longpalinsubstr("babad"))
