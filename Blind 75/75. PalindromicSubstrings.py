"""


Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Approach: as this is a palindromic substring question, always use helper function to start from the mid
add those to get the total count.

Tc: O(n) as we are iterating only once
Sc: O(1) as we only using res to store a number
"""


def countPalinSubstr(s):
    res = 0
    # doubt as we are doing it for every iteration don't we have the double count. ?
    for i in range(len(s)):
        res += palinSubstr(s, i, i)  # odd case
        res += palinSubstr(s, i, i+1)  # even case
    return res


def palinSubstr(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
        count += 1
    return count


print(countPalinSubstr("aaa"))
