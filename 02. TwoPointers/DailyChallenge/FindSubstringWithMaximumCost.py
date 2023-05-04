"""
https://leetcode.com/problems/find-the-substring-with-maximum-cost/

Approach - sliding window with Kadane algorithm

tc - O(n)
sc - O(n) 
"""

def maximumCostSubstring(s, chars, vals):
    dic = defaultdict(int)
    for i in range(len(char)): #add cost from vals array
        dic[chars[i]] = vals[i]
    for char in s: #add alphabetical cost if char cost is not given
        if char not in dic:
            dic[char] = (ord(char) - ord('a')) + 1
    total = 0
    res = 0
    for right in range(len(s)): #sliding window
        if total < 0: #kadane algo 
            total = 0
        total += dic[s[right]]
        res = max(res, total)
    return res