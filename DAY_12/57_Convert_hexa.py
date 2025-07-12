'''Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"'''





# LOgical code

class Solution(object):
    def toHex(self, num):
        """
        :type num: int   (32‑bit signed)
        :rtype: str
        """

        if num == 0:
            return "0"

        if num < 0:
            num += 1 << 32           

        hex_digits = "0123456789abcdef"
        result = []

        while num > 0:
            last_four_bits = num & 0b1111   
            result.append(hex_digits[last_four_bits])
            num >>= 4                        
        return "".join(reversed(result))



# My logic but not support negative

# def toHex(num):
#     if num < 0:
#         num += 2**32
#     return hex(num)[2:]







# Simple logic

# class Solution(object):
#     def toHex(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         if num == 0:
#             return "0"
        
#         num = num & 0xFFFFFFFF
        
#         mapping = "0123456789abcdef"
#         out = ""
        
#         while num > 0:
#             out = mapping[num % 16] + out 
#             num >>= 4
        
#         return out
        