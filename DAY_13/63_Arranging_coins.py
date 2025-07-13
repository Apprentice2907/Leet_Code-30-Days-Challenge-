'''You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 '''







# MY logic using pattern logic and then comparring the rows and last filled column 

# But memory limit reached

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         j = 0 
#         for i in range(1, n + 1):  
#             j = j + i             
#             if j == n:
#                 return i          
#             elif j > n:
#                 return i - 1      





# Using while loop

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        i = 1                 
        while n >= i:         
            n -= i            
            i += 1     
        j = n                

        if j < i:
            return i - 1      
        else:                 
            return i         
        



# Leet code Best Solution
# class Solution(object):
#     def arrangeCoins(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         left, right = 0, n
#         while left <= right:
#             mid = (left+right) // 2
#             total = mid*(mid+1)//2
#             if total == n:
#                 return mid
#             elif total < n:
#                 left = mid+1
#             else:
#                 right = mid-1
        
#         return right
        
        