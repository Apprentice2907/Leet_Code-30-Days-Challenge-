'''
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.
'''





#my logic  

class Solution:
    def hammingWeight(self, n):
        bit_string = bin(n)[2:]  
        count = 0
        for bit in bit_string:
            if bit == '1':
                count += 1
        return count



# from collections import Counter

# class Solution:
#     def hammingWeight(self, n):
#         bit_string = bin(n)[2:]          
#         count = Counter(bit_string)       
#         return count['1']                


