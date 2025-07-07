'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.'''






# Logical answer and best score

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)



#  My logic but not efficient

# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False

#         for ch in s:
#             if s.count(ch) != t.count(ch):
#                 return False

#         return True





# Other logics 

# from collections import Counter
# class Solution(object):
#     def isAnagram(self, s, t):
#         return Counter(s) == Counter(t)



# Adds and subtracts character frequencies simultaneously for s and t.
# If all elements in count are 0, the strings are anagrams.


# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
#         count = [0] * 26
#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1
#             count[ord(t[i]) - ord('a')] -= 1
#         return all(x == 0 for x in count)





# Build a frequency count from s.
# Reduce that count while reading t.
# If any count goes negative → not an anagram.



# class Solution(object):
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False

#         count = {}

#         for ch in s:
#             count[ch] = count.get(ch, 0) + 1

#         for ch in t:
#             if ch not in count:
#                 return False
#             count[ch] -= 1
#             if count[ch] < 0:
#                 return False

#         return True
