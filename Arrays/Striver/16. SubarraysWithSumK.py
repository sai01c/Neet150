"""
https://leetcode.com/problems/subarray-sum-equals-k/

Approach - we maintain a dic with all the prefix sums and its counts.
[1,1,1,1] k=3 here, prefix sum is 4 when we reach the last element but if we remove the 
first element from our prefix sum it will be equal to k. so if we maintain prefix sum we can
know how many such do we have

tc - n
sc - n

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        prefix = 0
        res = 0
        dic[prefix] = 1 
        #adding 0 because [1,1,1] k=3 we can remove 0 and our sum == k
        for num in nums:
            prefix += num
            diff = prefix - k
            res += dic[diff]
            dic[prefix] += 1
        return res