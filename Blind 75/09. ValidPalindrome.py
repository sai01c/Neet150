"""
https://leetcode.com/problems/valid-palindrome/

Approach: this is a palindrome questions so we have to use two pointers
we need to eliminate non-alphabetical so increase/decresse the pointers whenever you encounter them. 
next. we need to check is left == right

TC: O(n) as we are iterating once through the loop
Sc: O(1) we are using only pointers.

"""

def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():  # increasing if the pointer is not alnum
            left += 1
        elif not s[right].isalnum():  # decrease the pointer if not alnum
            right -= 1
        else:
            if s[left].lower() != s[right].lower():  # they asked for only lower case letters
                return False
            left += 1  # continue increasing the pointers until you complete the while
            right -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
