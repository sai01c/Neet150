"""
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

tc - O(n)
sc - O(n)
"""

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        
        while max(count.values()) > 0: #we do until count of any element is greater than 0
            row = [] #each iteration initialize empty array and keep adding to it
            for k, v in count.items():
                if v >= 1: #get all unique elements and add them to our row
                    row.append(k)
                    count[k] -= 1 #decrease the count of that element.
            res.append(row) #end of the iteration append row to our output
        return res