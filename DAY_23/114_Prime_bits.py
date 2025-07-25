'''Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101, which has 3 set bits.
 

Example 1:

Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.
Example 2:

Input: left = 10, right = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.'''













# My logic 

class Solution(object):
    def countPrimeSetBits(self, left, right):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

        count = 0
        for i in range(left, right + 1):
            bits = bin(i)[2:] 
            ones = 0
            for ch in bits:
                if ch == '1':
                    ones += 1
            if is_prime(ones):
                count += 1
        return count










# Leet code best solution

# class Solution(object):
#     def countPrimeSetBits(self, left, right):
        
#         prime_set = {2, 3, 5, 7, 11, 13, 17, 19}

#         count = 0
#         for num in range(left, right + 1):
           
#             set_bits = bin(num).count('1')
           
#             if set_bits in prime_set:
#                 count += 1

#         return count