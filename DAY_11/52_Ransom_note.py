'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true'''






# My logic but error while 'aab'=='baa' but false output

# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         if ransomNote in magazine:
#             return True
#         return False
        








class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for ch in ransomNote:
            if ch in magazine:
                magazine = magazine.replace(ch, '', 1) 
                return False
        return True










# Leet Code Best

# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         charCount = {}
#         for ch in magazine:
#             if ch in charCount:
#                 charCount[ch] += 1
#             else:
#                 charCount[ch] = 1
#         for ch in ransomNote:
#             if ch in charCount:
#                 if charCount[ch]>0:
#                     charCount[ch] -=1
#                 else:
#                     return False
#             else:
#                 return False
#         return True                 