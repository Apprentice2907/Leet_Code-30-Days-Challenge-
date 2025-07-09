'''Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
'''






# n=1 test case failed

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        temp = round(n ** (1.0 / 3))
        return 3 ** temp == n     
            



# n-243 test case failed ChatGPT

# import math

# class Solution(object):
#     def isPowerOfThree(self, n):
#         if n <= 0:
#             return False
#         x = math.log(n, 3)
#         return x.is_integer()




# n=243 test case failed

# class Solution(object):
    # def isPowerOfThree(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
        
    #     if n <= 0:
    #         return False
    #     x = math.log(n, 3)
    #     return x.is_integer()
    


# Accepted code

# class Solution(object):
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
        
#         while n > 1:
#             if n % 3 != 0:
#                 return False
#             n //= 3
#         return n == 1
    
            
        

# Leet code best solution
            
# class Solution(object):
#     def isPowerOfThree(self, n):
#         if n<=0:
#             return False
#         if n==1:
#             return True
#         if n%3!=0:
#             return False
#         return self.isPowerOfThree(n//3)
     
        