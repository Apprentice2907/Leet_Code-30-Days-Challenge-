'''The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
'''






# My logic and easy understanding 

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bits = bin(num)[2:]
        flipped = ''.join('0' if ch == '1' else '1' for ch in bits)
        return int(flipped, 2)
    





# Unique Logic 
# class Solution(object):
#     def findComplement(self, num):
#         n = num.bit_length()
#         mask = (1<<n)-1
#         return num^mask







# Binary Method

# class Solution(object):
#     def findComplement(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """

#         binary = []
#         i = 0 
#         while num != 0:
#             s = num%2
#             binary.append(s)
#             num = (num-s)/2
#             i += 1

#         binary = binary[::-1]
#         L = len(binary)
#         i = 0 
#         result = 0
#         while i < L :
#             binary[L - 1 - i] = 1 - binary[L - 1 -i]
#             result += (2**i)*(binary[L-1-i])
#             i += 1
#         return result

        