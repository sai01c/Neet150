"""
https://leetcode.com/problems/group-anagrams/

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""


def group(strs):
    count = {}
    res = []
    for word in strs:
        sortWord = "".join(sorted(word))
        if sortWord not in count:
            count[sortWord] = [word]
        else:
            count[sortWord].append(word)
    for val in count.values():
        res.append(val)

    return res


print(group(["eat", "tea", "tan", "ate", "nat", "bat"]))
