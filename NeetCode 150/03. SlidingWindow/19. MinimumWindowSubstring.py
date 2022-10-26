"""
https://leetcode.com/problems/minimum-window-substring/submissions/

Approach: First, we create a count dict for t string. 
using sliding window technique, we create new count dict for substring in s
initiate two variables have and need to measure the length of the dictionaries
as we need the minimum length, we as long as have = need we try to shift the left pointer. we also decrease the count for the left char. 
our resLen should be the as min as possible.  

Tc: O(n) linear according to neetcode why ???
but I think it is O(n^2) because of for and while
Sc: O(n) dictionary used here
"""


def minWinSubstr(s, t):
    tcount = {}
    subStrcount = {}

    for i in range(len(t)):
        tcount[t[i]] = tcount.get(t[i], 0) + 1

    have = 0
    need = len(tcount)

    left = 0
    resLen = float("infinity")

    for right in range(len(s)):
        char = s[right]
        subStrcount[char] = subStrcount.get(char, 0) + 1

        if char in tcount and tcount[char] == subStrcount[char]:
            have += 1 
            #here why not use subStrcount > tcount that should also satisfy
            #reason may be they are asking for min and we are doing while loop here 

        while have == need:
            if (right - left + 1) < resLen:
                resLen = right - left + 1
                res = s[left:right+1]
             #we need to remove left count as we already got minimum
                
            subStrcount[s[left]] -= 1

            if s[left] in tcount and subStrcount[s[left]] < tcount[s[left]]:
                have -= 1 #decrease have because we changed left count and out scount may vary now
            left += 1 #increase left because we already got min

    left, right = res
    return res if resLen != float("infinity") else ""


print(minWinSubstr("ADOBECODEBANC", "ABC"))
print(minWinSubstr("a", "a"))
