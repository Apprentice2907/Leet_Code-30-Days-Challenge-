'''Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If no such uncommon subsequence exists, return -1.

An uncommon subsequence between two strings is a string that is a subsequence of exactly one of them.


Example 1:

Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.
Example 2:

Input: a = "aaa", b = "bbb"
Output: 3
Explanation: The longest uncommon subsequences are "aaa" and "bbb".
Example 3:

Input: a = "aaa", b = "aaa"
Output: -1
Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a. So the answer would be -1.'''














# Logical and simple 

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        s1 = set()
        for i in range(len(a)):
            s = ""
            for j in range(i, len(a)):
                s+=a[j]
                s1.add(s)

        s2 = set()
        for i in range(len(b)):
            s = ""
            for j in range(i, len(b)):
                s+=b[j]
                s2.add(s)

        maxi = -1
        for i in s1:
            if i not in s2:
                maxi = max(maxi, len(i))
        
        maxi2 = -1
        for i in s2:
            if i not in s1:
                maxi2 = max(maxi2, len(i))
        return max(maxi, maxi2)



                









# Simple and easy logic

# class Solution(object):
#     def findLUSlength(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: int
#         """
#         if a == b:
#             return -1
#         return max(len(a), len(b))