"""
https://leetcode.com/problems/string-compression/

Approach: this is strings so use sliding window technique
if left, right are same we continue.
but if left != right, then calculate the length and move the left to right
there are couple of edge cases - if the right index is at last element of the array
if left != right in this case we do the same, we calculate the diff for first 
left and right and then we shift the left pointer to right. 
And, then if left == right, we calculate the difference and break

Tc: 
Sc: 

"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        i = 0
        for right in range(len(chars)):
            if right == len(chars) - 1 and chars[left] != chars[right]:
                chars[i] = chars[left]
                i += 1
                length = (right - left)
                if (length) > 1:
                    for j in str(length):
                        chars[i] = j
                        i += 1  
                left = right
            if right == len(chars) - 1 and chars[left] == chars[right]:
                chars[i] = chars[left]
                i += 1
                length = (right - left + 1)
                if length > 1:
                    for j in str(length):
                        chars[i] = j
                        i += 1
                    break
            
            if chars[left] == chars[right]:
                continue
            else:
                chars[i] = chars[left]
                i += 1
                length = (right - left)
                if (length) > 1:
                    for j in str(length):
                        chars[i] = j
                        i += 1  
                left = right
        
        return len(chars[:i])