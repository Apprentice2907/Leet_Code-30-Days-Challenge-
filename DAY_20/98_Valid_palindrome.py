'''Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false'''










# My logic but time limit exceeded

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(s):
            return s == s[::-1]

        if is_palindrome(s):
            return True

        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if is_palindrome(temp):
                return True

        return False
    













# ChatGPT logic and most optimal and efficient code

# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         def isPalindromeRange(left, right):
#             while left < right:
#                 if s[left] != s[right]:
#                     return False
#                 left += 1
#                 right -= 1
#             return True

#         left, right = 0, len(s) - 1

#         while left < right:
#             if s[left] != s[right]:
            
#                 return isPalindromeRange(left + 1, right) or isPalindromeRange(left, right - 1)
#             left += 1
#             right -= 1

#         return True