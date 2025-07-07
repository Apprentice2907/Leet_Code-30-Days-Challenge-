'''Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0'''






#  My logic but Chatgpt written
class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num








# Without using recursion or loops
#class Solution(object):
    # def addDigits(self, num):
    #     if num == 0:
    #         return 0
    #     return 1 + (num - 1) % 9
