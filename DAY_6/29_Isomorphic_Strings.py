'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true
'''






# My logic 
class Solution(object):
    def isIsomorphic(self, s, t):
        char_s = {ch: i for i, ch in enumerate(s)}
        map_s = [char_s[ch] for ch in s]

        char_t = {ch: i for i, ch in enumerate(t)}
        map_t = [char_t[ch] for ch in t]

        return map_s == map_t
    



# ChatGPT
# class Solution(object):
#     def isIsomorphic(self, s, t):
#         def build_pattern(string):
#             mapping = {}
#             pattern = []
#             index = 0
#             for ch in string:
#                 if ch not in mapping:
#                     mapping[ch] = index
#                     index += 1
#                 pattern.append(mapping[ch])
#             return pattern

#         return build_pattern(s) == build_pattern(t)



# Leetcode Best

# class Solution(object):
#     def isIsomorphic(self, s, t):
#         return len(set(zip(s,t)))==len(set(s))==len(set(t))

# s=Solution()
# s.isIsomorphic("paper","title")
