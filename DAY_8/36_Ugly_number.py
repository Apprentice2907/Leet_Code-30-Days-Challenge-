'''An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.'''




# My logic

# def isUgly(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n <= 0:
#             return False
#         for p in [2, 3, 5]:
#             while n % p == 0:
#                 n //= p
#         return n == 1
        



# Best leetcode solution

# class Solution(object):
#     def isUgly(self, n):
#         if n <= 0:
#             return False  
#         for i in [2, 3, 5]:
#             while n % i == 0:
#                 n //= i  
#         return n == 1 