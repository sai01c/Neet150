"""
https://leetcode.com/problems/number-of-1-bits/

Approach: we divide number with 2 that gives the remainder for last digit. now check 1 in this
then, shift the number to right by 1


"""

def hammingWeight(n):
    res = 0
    while n:
        remain = n % 2
        res += remain
        n = n >> 1
    return res