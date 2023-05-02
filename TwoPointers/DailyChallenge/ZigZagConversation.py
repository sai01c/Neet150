"""
https://leetcode.com/problems/zigzag-conversion/

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I


Solution: First go by row wise. In output, for this example you need 0, 6, 12th index elements. That means
you are incrementing by 12. which is 2 * numbear of rows - 1. For rows = 3, you'll increment by 4. 
Now, look at the second row, 1, 5, 7, 11, 13. As per previous observation, 1, 7 and 13 satisfy. But, here
you have additional 5 and 11. For all the middle rows you will have addditional elemnents. 
Now, if you look at 5 and 11 you are subtracting 2 from the increment i.e 6. 2 = 2 * row index i.e 1
if you look at third row, 2, 4, 8, 10. 2 and 8 are expected. now, we would also look at increment 2. 
6 - 2(2) = 2. 

Basically, for the top and bottom rows you use the original increment. But, for the middle rows we change
the increment. we also add other conditions. new increment = iteration + original increment - 2 * row index. 
 
For, middle rows, we add both initial increment and new increment. 

Tc: O(number of rows * len(s)

"""


def zigzag(s: str, n):
    if len(s) == 1:
        return s
    res = ''
    for r in range(n):
        increment = 2 * n - 2
        for i in range(r, len(s), increment):
            res += s[i]


            if ( r > 0 and 
            r < n - 1 and
            (i + increment - 2 * r) < len(s)
            ):
                res += s[i + increment - 2 * r]
    return res

print(zigzag("PAYPALISHIRING", 3))
print(zigzag("PAYPALISHIRING", 4))
