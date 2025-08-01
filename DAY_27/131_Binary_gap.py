'''Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

 

Example 1:

Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
Example 2:

Input: n = 8
Output: 0
Explanation: 8 in binary is "1000".
There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.
Example 3:

Input: n = 5
Output: 2
Explanation: 5 in binary is "101".'''




# My logic 

class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        max_dist = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                for j in range(i + 1, len(binary)):
                    if binary[j] == '1':
                        if '1' not in binary[i+1:j]:
                            max_dist = max(max_dist, j - i)
                        break
        return max_dist




# Leetcode best solution

# class Solution(object):
#     def binaryGap(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         index=[]
#         s=str(bin(n))
#         for i in range(len(s)):
#             if s[i]=='1':
#                 index.append(i)
#         if len(index)==1:
#             return 0
#         dist=[index[i+1]-index[i] for i in range(len(index)-1)]
#         return max(dist)
            
    
        
            