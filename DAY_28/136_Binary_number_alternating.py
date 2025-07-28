'''Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
 '''







# My logiv for this problem leetcode best 

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)[2:] 
        for i in range(len(binary) - 1):
            if binary[i] == binary[i + 1]:
                return False
        return True
    

# Different logic

# class Solution(object):
#     def hasAlternatingBits(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
        
#         x = n ^ (n >> 1)
#         return (x & (x + 1)) == 0