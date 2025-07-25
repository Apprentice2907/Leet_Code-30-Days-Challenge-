'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false'''






# Without using recursion or loops, using bit manipulation
# return n > 0 and (n & (n - 1)) == 0




#  My logic but time limit exceeded

class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        for i in range(0, n): 
            if 2 ** i == n:
                return True
        return False





# ChatGPT logic, which is more efficient

# class Solution(object):
#     def isPowerOfTwo(self, n):
#         if n <= 0:
#             return False
#         while n % 2 == 0:
#             n = n // 2
#         return n == 1