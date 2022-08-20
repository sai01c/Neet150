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
    if digits == []:
        return [1]

    if digits[-1] == 9:
        digits = plusOne(digits[:-1])
        digits.extend([0])

    else:
        digits[-1] += 1

    return digits


print(plusOne([1, 2, 3, 9]))
