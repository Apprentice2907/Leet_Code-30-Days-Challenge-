'''The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1'''







# Fast and logical

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = format(x, '032b')
        by = format(y, '032b')

        
        distance = 0
        for i in range(32):
            if bx[i] != by[i]:
                distance += 1

        return distance






# Easy logic

# class Solution(object):
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         xor = x ^ y  
#         count = 0
#         while xor:
#             if xor & 1:      
#                 count += 1
#             xor = xor >> 1  
#         return count
