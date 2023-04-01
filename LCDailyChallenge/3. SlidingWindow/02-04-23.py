"""
https://leetcode.com/problems/permutation-in-string/

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Solution: this is a substring problem so use sliding window concept (left, right pointers)
this is permutation problem, so use dictionary to store count/frequency.
Now, as we move through the right pointer, we add count of it. 
and, check if two count dict's are equal. 
Next, we need to add conditions for sliding window, if length of substring increases from the s1, then
remove left count and increase left pointer. 
We need to address edge case where we decrease the left count by 1 but left will remain in the dict with 0 as value. 
then this does not satisfy our check to equate dicts. 
so, we check if the count of left is 0 then we delete that key i.e left from count dict.

TC: O(s1 + s2)
Sc: O(s1+ s2)

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1count = {}
        for i in s1:
            s1count[i] = s1count.get(i, 0) + 1
        
        s2count = {}
        for right in range(len(s2)):
            s2count[s2[right]] = s2count.get(s2[right], 0) + 1
            sub = s2[left: right+1]
            if s2count == s1count:
                return True
            
            if len(sub) >= len(s1):
                s2count[s2[left]] -= 1
                if s2count[s2[left]] == 0: del s2count[s2[left]] #this is the edge case we referred above. 
                left += 1
                
        return False
        