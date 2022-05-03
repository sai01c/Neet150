"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Explanation: this is a substring problem so we need to use sliding window technique. 
we use a set to keep the unique characters.
until we have unique we keep removing the left characters. 

TC: O(n^2) as we are using while inside for loop
SC: O(n) for set
"""


def uniqueSubstring(s):
    left = 0
    ans = 0
    temp = set()  # we can also use a list here but removal from set is O(1)
    for right in range(len(s)):
        # we want to make sure we only have unique in temp before we add right
        while s[right] in temp:
            # notice while here- we want to make sure everything is unique in temp
            temp.remove(s[left])
            left += 1
        temp.add(s[right])
        # we want length here, left and right are indexes so we add 1.
        ans = max(ans, right - left + 1)
    return ans


print(uniqueSubstring("bbbbb"))
