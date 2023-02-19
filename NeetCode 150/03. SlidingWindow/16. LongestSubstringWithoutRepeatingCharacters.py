"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Explanation: this is a substring problem so we need to use sliding window technique. 
we use a set to keep the unique characters.
until we have unique we keep removing the left characters. 

TC: O(n) as we are using while inside for loop
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

"""
Same approach as 1 but instead of using set we are using map and checking if count is more than
1. Same TC and SC
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        count = {}
        for right in range(len(s)):
            sub = s[left:right+1]
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
                
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
            
            ans = max(ans, right-left+1)
            
        return ans