'''Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.'''







# My logic using string complex logic

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        n = len(s)
        for i in range(1, n):
            sub = s[:i] 
            if sub * (n // len(sub)) == s:
                return True
        return False










# Easy logic and works like
'''For "abab":
s + s = "abababab"
Remove first and last → "bababa"
Check if "abab" is in "bababa"'''

# class Solution(object):
#     def repeatedSubstringPattern(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """        
#         return s in (s + s)[1:-1]
