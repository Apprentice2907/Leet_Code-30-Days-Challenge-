'''A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]'''







# my logic using for loop and conditional statement


# class Solution(object):
#     def diStringMatch(self, s):
#         """
#         :type s: str
#         :rtype: List[int]
#         """
        
#         low = 0
#         high = len(s)
#         res = []

#         for ch in s:
#             if ch == 'I':
#                 res.append(low)
#                 low += 1
#             else:
#                 res.append(high)
#                 high -= 1

#         res.append(low)
#         return res











# leet code best solution

# class Solution(object):
#     def diStringMatch(self, s):
#         """
#         :type s: str
#         :rtype: List[int]
#         """
#         i=0
#         j=len(s)
#         ar=[]
#         for no in s:
        

#                 if no=='I':
#                     ar.append(i)
#                     i+=1
                    
#                 else:
#                     ar.append(j)
#                     j-=1
#         ar.append(i)
#         return ar

        