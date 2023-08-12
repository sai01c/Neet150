"""
https://leetcode.com/problems/permutation-in-string/


Approach: first we iterate through the length of the s1 and 
add count of the s1 string to s1 count array and s2 string to s2 count 
array. Here if the length of s1 is 3 we only take count of the first three
characters of the string s2

now, in s1 count and s2 count - if the string is abde
then [1,1,0,1,1,0,0,....0] length of the count array will be 26. 

Now, as this is a substring problem - we take sliding window concept
and increase the s2count by adding right count and subracting left count
we increase the left pointer every iteration.

if the len of s1 is 3 then we start the right pointer at 3. 
so the substring len is 3 (right - left) 

Tc: O(26n) comparing 26 length arrays
Sc: O(n) arrays

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = Counter(s1)
        dic2 = {}
        l = 0
        for r in range(len(s2)):
            val = s2[r]
            if val in dic2:
                dic2[val] += 1
            else:
                dic2[val] = 1
            length = r - l + 1
            
            if length == len(s1):
                if dic1 == dic2:
                    return True
                dic2[s2[l]] -= 1
                if dic2[s2[l]] == 0:
                    del dic2[s2[l]]
                l += 1
        return False
            