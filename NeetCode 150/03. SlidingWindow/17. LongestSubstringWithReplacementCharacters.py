"""
https://leetcode.com/problems/longest-repeating-character-replacement/

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Approach: as it is a substring problem, we want to use a sliding window.
here the condition is we can make k replacements
we can store the frequency of substring characters using count dictionary
basically our substring length = max(count of character) + k
if length - max > k then we need to decrease the length of our substring. 

TC: O(n) we are iterating using the for loop 
Sc: O(n) we are using count dictionary for storing the frequency
"""


def substringKreplace(s, k):
    left = 0
    count = {}
    ans = 0
    for right in range(len(s)):
        # to get the frequency of the substring
        count[s[right]] = count.get(s[right], 0) + 1
        if (right-left+1) - max(count.values()) > k:  # our base condition is length - max = k
            # we can also use if here instead of while ???
            # if is used here because repeating characters are allowed.
            # while is used when repeating characters are not allowed.
            # as we are iterating right by 1 each time I don't think while is required
            count[s[left]] -= 1  # we cut short the substring
            left += 1
            ans = max(ans, right-left+1)
    return ans


print(substringKreplace("AABABBA", 1))
