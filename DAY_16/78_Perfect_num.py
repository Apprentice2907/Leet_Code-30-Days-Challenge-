'''A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.


Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 7
Output: false'''














# Simple and easy logic but memory limit exceeded

def checkPerfectNumber(num):
    if num <= 1:
        return False

    sum_divisors = 1
    for i in range(2, num):
        if num % i == 0:
            sum_divisors += i

    return sum_divisors == num









# Leetcode best solution

# class Solution(object):
#     def checkPerfectNumber(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num <= 1:
#             return False
        
#         sum = 1
#         i = 2
#         while i * i <= num:
#             if num % i == 0:
#                 sum += i
#                 if i != num // i:
#                     sum += num // i
#             i += 1
#         return sum == num
        









# ChatGPT solution

# class Solution(object):
#     def checkPerfectNumber(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num <= 1:
#             return False

#         sum_divisors = 1 
#         i = 2

#         while i * i <= num:
#             if num % i == 0:
#                 sum_divisors += i
#                 if i != num // i: 
#                     sum_divisors += num // i
#             i += 1

#         return sum_divisors == num