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
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        dic = defaultdict(int)
        res = 0
        for r in range(len(fruits)):
            dic[fruits[r]] += 1
            
            while len(dic) > 2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    del dic[fruits[l]]
                l += 1
            
            temp = 0
            for v in dic.values():
                temp += v
            
            res = max(res, temp)
        
        return res
