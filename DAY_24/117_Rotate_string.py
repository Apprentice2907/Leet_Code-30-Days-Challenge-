'''Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false'''








# MY logic simple and easy to understand

class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            rotated = s[i:] + s[:i]  
            if rotated == goal:
                return True
        return False




# Another logic

# class Solution(object):
#     def rotateString(self, s, goal):
#         """
#         :type s: str
#         :type goal: str
#         :rtype: bool
#         """
#         y=list(s.strip())
#         print(y)
#         g=list(goal.strip())
#         for i in range(len(s)):
#             x=y.pop(0)
#             y.append(x)
#             if y==g:
#                 return True
#         return False






# class Solution(object):
#     def rotateString(self, s, goal):
#         i=0
#         while(i<len(goal) and (s!=goal)):

#             s=s[len(s)-1]+s
#             s=s[0:len(s)-1:1]
#             i+=1
        
#         return s==goal
        