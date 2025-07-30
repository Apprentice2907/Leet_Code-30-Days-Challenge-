'''Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"'''










# My logic but chatGPT coded and leetcode best solution

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = ''
        for ch in s:
            if ch.isalpha():
                rev = ch + rev 

        result = ''
        rev_index = 0

        for ch in s:
            if ch.isalpha():
                result += rev[rev_index]
                rev_index += 1
            else:
                result += ch

        return result
            









# Exact logic i proposed but chatGPT coded
#     rev = s[::-1]
#     rev_letters = ''
#     for ch in rev:
#         if ch.isalpha():
#             rev_letters += ch

#     lengths = []
#     temp_len = 0
#     for ch in s:
#         if ch.isalpha():
#             temp_len += 1
#         else:
#             if temp_len > 0:
#                 lengths.append(temp_len)
#                 temp_len = 0
#     if temp_len > 0:
#         lengths.append(temp_len)

#     result = ''
#     rev_idx = 0
#     s_idx = 0
#     word_idx = 0
#     letter_count = 0

#     while s_idx < len(s):
#         if s[s_idx].isalpha():
#             result += rev_letters[rev_idx]
#             rev_idx += 1
#             letter_count += 1
#             if word_idx < len(lengths) and letter_count == lengths[word_idx]:
#                 word_idx += 1
#                 letter_count = 0
#         else:
#             result += s[s_idx]
#         s_idx += 1

#     return result