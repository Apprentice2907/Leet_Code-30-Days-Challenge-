'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false'''







# class Solution(object):
#     def isSubsequence(self, s, t):
#         i = 0  # pointer for s
#         for ch in t:
#             if i < len(s) and s[i] == ch:
#                 i += 1
#         return i == len(s)




# MY logic
class Solution(object):
    def isSubsequence(self, s, t):
        index = -1  #

        for ch in s:
            index = t.find(ch, index + 1) 
            if index == -1:
                return False 
        return True







# ChatGPT solution

# class Solution(object):
#     def isSubsequence(self, s, t):
#         prev_index = -1

#         for ch in s:
#             found = False
#             for i in range(prev_index + 1, len(t)):
#                 if t[i] == ch:
#                     prev_index = i
#                     found = True
#                     break
#             if not found:
#                 return False
#         return True












'''Logic

Initialize a variable prev_index to -1.
This keeps track of the index of the last matched character from s in t.

Loop through each character ch in s:

For each ch, scan t from prev_index + 1 onward.

As soon as you find a match t[i] == ch, update prev_index = i.

This ensures every next character in s appears after the previous one in t.

If the character is not found in the rest of t:

Set a found flag to False.

If found remains False after the inner loop, return False immediately — this means s is not a subsequence of t.

If the loop completes successfully, it means all characters of s were found in order in t, so return True.'''