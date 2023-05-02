"""
https://leetcode.com/problems/naming-a-company/

Approach: This is very tricky question. I first solved using two for loops with i and j iterating over the array in n^2. This gave TLE.
Create a hashset with key as first string, value as the rest of the string. 
using hashset instead of hashmap with array because set search is O(1).
using default dic because it won't throw an index out of range error if our key is not already present.

Now, coming to main logic, we will iterate over the hashset using two pointers. 
think of it this way - if there are two array's - [a, b], [c, d]. 
we can form ac, ad, bc, bd if no intersection. Also, reverse of these can be formed but that won't be counted now. len(arr1) * len(arr2) = 4
if there are intersections - [a,b], [c, b] then we can only form ac, bc. len(arr1) * len(arr2) - intersection in arr1 - intersection in arr2.

in the same way we will iterate reverse order as well. we used two for loops here. 

TC: O(26 n)
Sc: O(n).
"""

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic = collections.defaultdict(set)
        res = 0
        for idea in ideas:
            dic[idea[0]].add(idea[1:])

        for char1 in dic: #26
            for char2 in dic: #26
                if char1 == char2:
                    continue
                    
                intersect = 0
                for val in dic[char1]: #O(n)
                    if val in dic[char2]:
                        
                        intersect += 1
                        
                temp1 = len(dic[char1]) - intersect
                temp2 = len(dic[char2]) - intersect
                
                res += temp1 * temp2
                
        return res
        
