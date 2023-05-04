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
        left = 0
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        for char in s1:
            c1[char] += 1
        for right in range(len(s2)):
            sub = s2[left:right+1]
            c2[s2[right]] += 1
            
            if c1 == c2:
                return True
            print(c2)
            if len(sub) == len(s1):
                c2[s2[left]] -= 1
                if c2[s2[left]] == 0: del c2[s2[left]]
                left += 1
                
        return False