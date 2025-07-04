'''Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.'''



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        temp=str(x)
        temp=temp[::-1]
        temp=int(temp)
        if temp==x:
            return True
        else:
            return False

# Correct but verry slow and not efficient
#         original = x
#         rev = 0
#         while x > 0:
#             digit = x % 10
#             rev = rev * 10 + digit
#             x //= 10
#         return original == rev
      

# Best Output:
# a = str(x)
#         return a[::-1]==a