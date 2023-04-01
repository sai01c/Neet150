"""

https://leetcode.com/problems/add-binary/

Approach: 
This is regular addition but base 2 as binary
Now, we create two pointers i and j we go from reverse direction
until the pointer reach 0th index, we add and apply the carry
at the end we reverse the direction.


Tc: O(n)


"""

def addBinary(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    res = ""
    while i >= 0 or j>= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        res += str(total % 2)
        carry = total // 2

    return res[::-1]

