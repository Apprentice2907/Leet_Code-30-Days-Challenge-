'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1'''






# My logic but not time efficient

# class Solution(object):
#     def firstUniqChar(self, s):
#         for i in range(len(s)):
#             if s.count(s[i]) == 1:
#                 return i
#         return -1






# ChatGPT

# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         O(n) time, O(1) extra space (26 counters).
#         """
#         freq = [0] * 26
#         for ch in s:                       
#             freq[ord(ch) - 97] += 1

#         for i, ch in enumerate(s):        
#             if freq[ord(ch) - 97] == 1:
#                 return i

#         return -1







# Dictionary  

def firstUniqChar(self, s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1





# Leetcode solution

# class Solution(object):
#     def firstUniqChar(self, s):
#         count=Counter(s)
#         for i,ch in enumerate(s):
#             if count[ch]==1:
#                 return i
#         return -1