'''Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 '''










class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        root = int(num ** 0.5 + 0.5)
        return root * root == num


# safer: Use math.isqrt()

# import math
# class Solution(object):
#     def isPerfectSquare(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         root = int(math.isqrt(num))
#         return root * root == num



#Binary Search best space complexity 

# class Solution(object):
#     def isPerfectSquare(self, num):
#         if num < 2:
#             return True
#         left, right = 2, num // 2
#         while left <= right:
#             mid = (left + right) // 2
#             square = mid * mid
#             if square == num:
#                 return True
#             elif square < num:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return False
