'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true'''


class Solution(object):
    def isValid(self, s):
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""


# Most efficient solution ChatGPT

# class Solution(object):
#     def isValid(self, s):
#         stack = []
#         mapping = {')': '(', ']': '[', '}': '{'}

#         for char in s:
#             if char in mapping:
#                 top = stack.pop() if stack else '#'
#                 if mapping[char] != top:
#                     return False
#             else:
#                 stack.append(char)

#         return not stack



# Most efficient solution LeetCode


# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         for i in s:
#             if i in ["(","{","["]:
#                 stack.append(i)
#             elif stack:
#                 if i == "]":
#                     if stack[-1] != "[":
#                         return False
#                     stack.pop()
#                 elif i == "}":
#                     if stack[-1] != "{":
#                         return False
#                     stack.pop()
#                 elif i == ")":
#                     if stack[-1] != "(":
#                         return False
#                     stack.pop()
#             else:
#                 return False
#         if stack: return False
#         return True



sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))     
print(sol.isValid("{[]}"))     
