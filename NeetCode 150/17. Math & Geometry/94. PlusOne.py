"""
https://leetcode.com/problems/plus-one/

APPROACH: 
we might have two cases - 
last digit is 9 - we want to use recurssion, excluding the 9. and then extend with 0
last digit is not 9 - we can add 1 to the last element 


TC: O(n) to confirm
SC: O(1)
"""


def plusOne(digits):
    if digits == []: #if null array we need to add 1
        return [1]

    if digits[-1] == 9: #last digit is 9 then do recursion excluding last digit
        digits = plusOne(digits[:-1])
        digits.extend([0]) #and then append 0

    else: #if not 9 simply add 1 to the last digit
        digits[-1] += 1

    return digits


