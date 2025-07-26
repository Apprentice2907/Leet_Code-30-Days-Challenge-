'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".'''







# My logic

class Solution(object):
    def backspaceCompare(self, s, t):
        sresult = []
        for ch in s:
            if ch == '#':
                if sresult:
                    sresult.pop()
            else:
                sresult.append(ch)

        tresult = []
        for ch in t:
            if ch == '#':
                if tresult:
                    tresult.pop()
            else:
                tresult.append(ch)

        return sresult == tresult







# Leetcode Best Solution

# class Solution(object):
#     def backspaceCompare(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         stack = []
#         stack1 = []

#         for char in s:
#             if char != '#':
#                 stack.append(char)
#             elif stack:
#                 stack.pop()

#         for char1 in t:
#             if char1 != '#':
#                 stack1.append(char1)
#             elif stack1:
#                 stack1.pop()

#         return stack == stack1





