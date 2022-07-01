"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach- this is a sliding window problem 
we iterate over the array with two pointers
use an array to check for unique characters 

Tc: O(n^2)
Sc: O(n) array

"""


def funct(s):
    left = 0
    ans = 0
    uniqueArray = []
    for right in range(len(s)):  # iterating over the array
        while s[right] in uniqueArray:
            # idea is to remove the characters from the string from left
            # while is used as repeating characters are not allowed and we want to have unique elements only
            uniqueArray.remove(s[left])
            left += 1
        uniqueArray.append(s[right])
        ans = max(ans, right-left + 1)
    return ans


print(funct("abcabcbb"))
