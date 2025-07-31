'''Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 '''








# My logic and time limit exceeded

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxp = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a = nums[i]
                    b = nums[j]
                    c = nums[k]
                    if a + b > c and a + c > b and b + c > a:
                        p = a + b + c
                        if p > maxp:
                            maxp = p
        return max





# class Solution(object):
#     def largestPerimeter(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort(reverse=True)
#         for i in range(len(nums) - 2):
#             a = nums[i]
#             b = nums[i + 1]
#             c = nums[i + 2]
#             if b + c > a:
#                 return a + b + c
#         return 0









# Leet code best solution

# class Solution(object):
#     def largestPerimeter(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort(reverse=True)
        
#         for i in range(len(nums)-2):
#             a,b = nums[i], nums[i+1]+nums[i+2]
#             if a<b:
#                 return a+b
#         return 0        