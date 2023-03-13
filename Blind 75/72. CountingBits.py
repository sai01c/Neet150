"""
https://leetcode.com/problems/counting-bits/

Approach: we take the number and add it to decimal array.
for number in decimal we take the remainder and update the number by dividing by 2

"""

def countBits(n):
    decimal , binary = [], []
    for i in range(n+1):
        decimal.append(i)

    for d in decimal:
        ones = 0
        while d > 0:
            remain = d % 2
            ones += remain
            d = d // 2
        binary.append(ones)
    
    return binary