"""
https://leetcode.com/problems/jump-game-ii/

Approach: This is very tricky question. Using greedy approach.
First, think of it this way. we will have two pointer's left and right - now left will just increase by 1, but right will 
increase to the maximum that is possible. Now we will have one level added. 
In the same way we repeat until right reaches the end. we can just count number of levels we added. 

Tc: Neetcode mentioned O(n) but I don't know how? 
Sc: O(1)

"""

def jumpGame(nums):
  left = 0
  right = 0
  res = 0
  while right < len(nums) - 1:
    far = 0
    for i in range(left, right + 1):
      far = max(far, nums[i] + i)
      
    left = right + 1
    right = far
    
    res += 1
    
  return res
