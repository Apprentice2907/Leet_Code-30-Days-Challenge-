'''Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''








# My logic

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n + 1):
            count = 0
            num = i
            while num > 0:
                count += num & 1  
                num >>= 1        
            result.append(count)
        return result









# Same logic but optimized code 

# class Solution(object):
#     def countBits(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         result = []
#         for i in range(n + 1):
#             binary = bin(i)          
#             count = binary.count('1') 
#             result.append(count)
#         return result
    





# Leet code best solution

# class Solution(object):
#     def countBits(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """

#         ans = [0]*(n+1)
#         for i in range(1, n + 1):
#             ans[i] = ans[i >> 1] + (i & 1)
#         return ans
        

            
        