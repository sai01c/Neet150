"""
https://leetcode.com/problems/koko-eating-bananas/

already part of neetcode 150

https://leetcode.com/problems/maximum-product-of-three-numbers/

APPROACH: first sort the numbers and find the product of last three numbers. If numbers are negative, 
find the two least numbers and the highest number.
Tc: O(n), Sc: O(1)
"""

def maxOf3Num(nums):
    nums.sort()
    a = nums[-1] * nums[-2] * nums[-3]
    b = nums[0] * nums[1] * nums[-1]

    return max(a, b)

"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Approach: Before adding check if the current char == last value in stack. 
if yes remove it. if not just append it to the stack. this is greedy solution

Tc: O(n), Sc: O(n) stack
"""

def removeDuplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        
        else:
            stack.append(char)
    res = ""
    for char in stack:
        res += char
    return res

"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Approach: check if last index is same as char, then get the count of last index and add 1. now, if the 
count is == k, then pop k times. 
If the char is not equal append to stack and add count as 1.
"""

def removeDuplicates(s, k):
    stack = []
    for char in stack:
        if stack and stack[-1][0] == char:
            count = stack[-1][1]
            stack.append((char, count+1))
            if stack[-1][1] == k:
                for i in range(k):
                    stack.pop()
        else:
            stack.append((char, 1))
    res = ""
    for char, count in stack:
        res += char
    return res
    