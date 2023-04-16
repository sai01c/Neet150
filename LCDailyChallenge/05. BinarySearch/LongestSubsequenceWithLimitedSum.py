"""
https://leetcode.com/problems/longest-subsequence-with-limited-sum/

Approach - prefix sum + binary search

tc nlogn
sc n

"""

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()  # sort the input list of numbers
        res = []     
        pre = []     # initialize the prefix sum list
        cum = 0      # initialize the cumulative sum variable
        for num in nums:
            cum += num           # add the current number to the cumulative sum
            pre.append(cum)      # append the cumulative sum to the prefix sum list

        for q in queries:
            l, r = 0, len(pre) - 1   
            ans = -1                 
            while l <= r:            
                mid = (l + r) // 2   
                if q < pre[mid]:
                    r = mid - 1       
                else:
                    #updating here because we want the max list that is less than q
                    ans = mid        
                    # update the answer if q is greater than or equal to the middle prefix sum
                    l = mid + 1      
            res.append(ans+1)         
            # append the answer to the result list (add 1 to get 1-based index)

        return res
