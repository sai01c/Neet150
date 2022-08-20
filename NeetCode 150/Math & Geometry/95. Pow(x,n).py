"""

APPROACH: 


TC: O(n)
SC: O(1)

"""


def pow(x, n):

    ans = helper(x, abs(n))  # pass absolute as there can be negative
    return ans if n > 0 else 1/ans


def helper(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    res = helper(x, n//2)
    res *= res  # we multiply because we divide by 2 above
    if n % 2 == 0:  # even
        return res
    else:  # odd number
        return res * x


print(pow(2.00, -2))
