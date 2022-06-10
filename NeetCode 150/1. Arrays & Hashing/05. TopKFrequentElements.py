"""
https://leetcode.com/problems/top-k-frequent-elements/

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Approach: first, use a count dictionary i.e element:frequenctcount
now, sort them in decreasing order of count
now iterate through the sort list and append the key i.e element

Tc: O(n) iterating over the list
Sc: O(n) using dictionary and res array
 
this was also mentioned under heaps
neetcode also gave similar soution. 
try to find heap solution
"""


def topKfrequent(nums, k):
    count = {}
    res = []
    for num in nums:
        count[num] = count.get(num, 0) + 1
    sortCount = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print(sortCount)
    for i in range(k):
        res.append(sortCount[i][0])
    return res


print(topKfrequent([1, 1, 1, 10,  2, 2, 3], 2))
