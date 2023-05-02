"""
https://leetcode.com/problems/fruit-into-baskets/

Explaination: First, we are given array of fruit types. Number of baskets is 2. 
This is like a substring problem. See it this way. You have main string and secondary string. 
Use left and right pointers to iterate through the array. Have a count dict. 
As you move right, add count to the dic. if the length of dic increases by 2, then remove the left count. 
Because you are only allowed to have 2 types. Handle edge case if count is 0, then delete that key. 
Now increase the left pointer. 
For each iteration, create a variable = 0 and add the two values from the dict. Now, use max condition to get the maximum of all the iterations.

Tc: for + while but this was given as O(n) in stack question by NeetCode. 
But, I think it is n^2 as in the while loop will run as long as len is more than 2. 
Sc: O(n) 

"""

def function(fruits):
  left = 0
  res = 0
  count = {}
  
  for right in range(len(fruits)):
    count[fruits[right]] = count.get(fruits[right]], 0) + 1
    
    while len(count) > 2:
      count[fruits[left]] -= 1
      if count[fruits[left]] == 0: del count[fruits[left]]
      left += 1
      
    temp = 0
    for v in count.values():
      temp += v
      
    res = max(res, temp)
    
  return res
