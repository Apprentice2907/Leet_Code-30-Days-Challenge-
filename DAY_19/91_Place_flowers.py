'''You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false'''







# My logic using mathematics ChatGPT coded

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0]
        i = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                count = 0
                while i < len(flowerbed) and flowerbed[i] == 0:
                    count += 1
                    i += 1
                
                n -= (count - 1) // 2
                if n <= 0:
                    return True
            else:
                i += 1

        return n <= 0
    









# Easy code

# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         for i in range(len(flowerbed)):
#             if (
#                 flowerbed[i] == 0 and
#                 (i == 0 or flowerbed[i - 1] == 0) and
#                 (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
#             ):
#                 flowerbed[i] = 1
#                 n -= 1
#                 if n == 0:
#                     return True
#         return n <= 0

