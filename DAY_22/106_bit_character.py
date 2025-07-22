'''We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.'''






# My logic simliar

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2  
            else:
                i += 1  
        return i == len(bits) - 1






# Most effient solution ChatGPT

# class Solution(object):
#     def isOneBitCharacter(self, bits):
#         i = 0
#         while i < len(bits) - 1:
#             i += 2 if bits[i] == 1 else 1
#         return i == len(bits) - 1
















# Leet code best solution

# class Solution:
#     def isOneBitCharacter(self, bits):
#         """
#         :type bits: List[int]
#         :rtype: bool
#         """
#         i = 0
#         n = len(bits)
        
#         while i < n - 1:
#             if bits[i] == 1:
#                 i += 2  # Skip the next bit as it's part of a two-bit character
#             else:
#                 i += 1  # Move to the next bit
        
#         # If we end up at the last position, it means the last character is one-bit
#         return i == n - 1