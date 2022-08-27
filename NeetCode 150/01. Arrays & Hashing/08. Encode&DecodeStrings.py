"""
https://www.lintcode.com/problem/659/

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Approach: Idea is to have the length and the keyword before the each string. 
Once you slice the length, then you know how many characters to slice. 
you are also adding # to next of string, we know when the length ends.
Create two pointers (start and end) and break the strings based on the length and keyword.

TC: O(n^2) two while loops but NEETCODE said O(n) 
SC: O(n) for res array
"""


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""
        for s in strs:

            res += str(len(s)) + "#" + s
        return res  # "4#lint4#code4#love3#you" this is the res now.

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        i = 0
        res = []
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1:j+length+1])
            i = j+1+length
        return res


obj = Solution()
res = (obj.encode(["lint", "code", "love", "you"]))
print(obj.decode(res))


class Solutionn:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        strings = ""
        for s in strs:
            strs += str(len(s)) + "#" + s
        return strings  # "4#lint4#code4#love3#you" this is the res now.

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        start = 0
        res = []
        while start < len(str):
            end = start
            while end != "#":
                end += 1
            length = str[start:end]
            res.append(str[end+1: end+1 + length])
            start = end+length+1
        return res


objj = Solutionn()
res = (objj.encode(["neet", "code", "love", "you"]))
print(objj.decode(res))
