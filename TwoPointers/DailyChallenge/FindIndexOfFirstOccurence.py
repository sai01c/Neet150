"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

approach: this is a sliding window algorithm. we assign left, right
now, while iterating using right, if the length of substring is more than needle
we increase the left pointer.

Tc: O(n) sliding window generally O(n)
Sc: O(1) constant space. 
"""

def func(haystack, needle):
    left = 0
    for right in range(len(haystack)):
        substring = haystack[left:right+1]
        if substring == needle:
            return left
        if len(haystack) >= len(needle):
            left += 1
    return -1