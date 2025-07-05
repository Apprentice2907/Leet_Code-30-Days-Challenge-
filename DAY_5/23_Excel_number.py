'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
'''





class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
        return result



# class Solution(object):
#     def titleToNumber(self, columnTitle):
#         """
#         :type columnTitle: str
#         :rtype: int
#         """
#         res = 0
#         for c in columnTitle:
#             res = res * 26 + ord(c) - 64
#         return res



