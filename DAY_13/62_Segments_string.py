'''Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

 

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1'''


# Simple ,easy my logic

# class Solution(object):
#     def countSegments(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
       
#         words = s.split() 
#         return len(words)




# Leet Code best

# class Solution(object):
#     def countSegments(self, s):
#             a = s.split(" ")
#             a = [x for x in a if x != ""]
#             return len(a)
        




# BEst Time complexity (ChatGPT)
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
      
        in_word = False
        count = 0

        for ch in s:
            if ch.isspace():
                in_word = False
            elif not in_word:
                count += 1
                in_word = True

        return count


