"""
https://leetcode.com/problems/valid-anagram/


Approach: store the frequency of characters in count dictionary. 
iterate over the s to add the frequency to count dictionary. 
iterate over the t to delete the frequency to count dictionary. 
now the count should become zero.

Tc: O(n) as we are iterating over s and t
Sc: O(n) as we are using a dictionary
"""

def valid(s, t):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count:
            return False
        else:
            count[char] -= 1
    for value in count.values():
        if value != 0:
            return False
    return True

def valid2(s, t):
    count_s = Counter(s)
    count_t = Counter(t)

    return count_s == count_t

print(valid("anagram", "nagaram"))
print(valid("rat", "car"))
