"""
https://leetcode.com/problems/number-of-zero-filled-subarrays/

Approach - while iterating if we see other than 0 we put count as 0.
now, if we see 0 we'll increase count by 1 and add to res.
let us say our zero subarray length is 0 - then number of subarray are 0+1
if length is 2 - total 3. i = 0,1 => 0+1 and 1+1 => 3
if length is 3 - total 6. i = 0,1,2 => 0+1, 1+1, 2+1 => 6
if length is 4 - total 10. i = 0,1,2,3 => 0+1, 1+1, 2+1, 3+1 => 10

Tc: O(n). Sc: O(1)

"""

def zeroFilledSubarray(nums): #optimal solution - Neetcode
    count = 0
    res = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
            res += count
        else:
            count = 0

    return res

def zeroFilledSubarray(nums): #non optimal solution- own
    sub = []
    res = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            sub.append(nums[i])
        else:
            if len(sub) > 0:
                for i in range(len(sub)): #this is the main logic
                    res += (i+1)
            sub = []
    
    if len(sub) > 0:
        for i in range(len(sub)):
            res += i+1
    
    return res