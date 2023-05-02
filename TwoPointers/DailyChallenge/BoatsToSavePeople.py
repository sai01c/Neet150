"""
https://leetcode.com/problems/boats-to-save-people/

Approach - Here, main logic is we can add only two people for one boat. we need the minimum number of boats
we sort the array and add the least and highest to one boat

tc O(nlogn)
sc O(1)
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() #sort the array first
        boats = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            total = people[left] + people[right]
            
            if total == limit: #two people can go into this boat
                left += 1
                right -= 1
                boats += 1
            elif total > limit: #only highest can go into this boat
                #right max is same as limit
                boats += 1
                right -= 1
            else: #two people can go into this boat
                left += 1
                right -= 1
                boats += 1
                
        return boats