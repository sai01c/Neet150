"""
https://leetcode.com/problems/optimal-partition-of-string/

Approach - we need to partition string and we need minimum number of partitions. So, we can optimize this
by having the length as max as possible for individual partitions.
substring problem so sliding window

tc - O(n)
sc - O(n)

"""

class Solution:
    def partitionString(self, s: str) -> int:
        visit = set() #using set because to check element is O(1)
        count = 0
        for right in range(len(s)):
            #this element is already there in set so increase the count and start set from 0 elements
            if s[right] in visit:
                count += 1
                visit = set()
                
            #add every element to our set
            visit.add(s[right])
        
        if visit: count += 1 #if there are any elements left in the set for last iteration elements
        return count