"""
https://leetcode.com/problems/top-k-frequent-elements/

Approach: instead of creating a frequency dictionary and sorting it.
create an array which has the frequency of elements.
max length of this frequency will be when each elemnt frequency is 1

Tc: O(n) solution #worst case it could be n^2 also ?
Sc: O(N)

"""

def func(nums, k):
    res = []
    freArray = [[] * len(nums)+1]
    count = Counter(nums) #dic with frequencies

    for num, fre in count.items(): #index is frequency. insert elements to the array
        freArray[fre].append(num)

    for array in range(len(freArray)-1, -1, -1):
        for i in array:
            res.append(i)
            if len(res) == k:
                return res
