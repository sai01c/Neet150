"""
https://leetcode.com/problems/valid-anagram/

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

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


print(valid("anagram", "nagaram"))
print(valid("rat", "car"))


"""
Approach: sort them and compare
TC: O(n logn) for sorting strings
SC: O(1) 

"""


def anagram(s, t):
    return sorted(s) == sorted(t)
