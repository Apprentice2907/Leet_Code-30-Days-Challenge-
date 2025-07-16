'''Given an integer num, return a string of its base 7 representation.

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"'''






class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        isneg = False
        if num < 0:
            isneg = True
            num = -num 

        result = ""
        while num > 0:
            result = str(num % 7) + result
            num //= 7

        return "-" + result if isneg else result
    






# Unique code from leetcode 

# class Solution(object):
#     def convertToBase7(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         res = [0] * 11
#         isNeg = num < 0
        
#         num = abs(num)
        
        
#         for n in range(10, -1, -1):
#             while pow(7, n) <= num:
#                 res[n] += 1
#                 num -= pow(7, n)
            
#             res[n] = str(res[n])
        
#         finalInt = int("".join(res[::-1]))
        
#         if isNeg:
#             finalInt *= -1
#         return str(finalInt)
        
        