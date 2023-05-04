"""
https://leetcode.com/problems/longest-repeating-character-replacement/

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
            count[s[left]] -= 1  # we cut short the substring
            left += 1
        ans = max(ans, right-left+1) #here we need to take the updated left pointer.
    return ans


print(substringKreplace("AABABBA", 1))
