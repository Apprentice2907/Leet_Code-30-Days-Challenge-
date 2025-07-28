'''An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 '''






# My logic using looping and conditional statement

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inc = True
        dec = True

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                dec = False
            elif nums[i] > nums[i + 1]:
                inc = False

        return inc or dec
    






# Best leet code solution

# class Solution(object):
#     def isMonotonic(self, nums):
#         n=len(nums)
#         increasing =True
#         decreasing=True
#         for i in range(1,n):
#             if(nums[i]>nums[i-1]):
#                 decreasing=False
#             if(nums[i]<nums[i-1]):
#                 increasing=False
#         return increasing or decreasing








# Another logic in leetcode

# class Solution(object):
#     def isMonotonic(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         # [1,2,2,3]
#         is_increasing = None
#         flag = True
#         for i in range(1,len(nums)):
#             if flag and nums[i] > nums[i-1]:
#                 is_increasing = True
#                 flag = False
#             elif flag and nums[i] < nums[i-1]:
#                 is_increasing = False
#                 flag = False
#             elif not flag and is_increasing:
#                 if nums[i] < nums[i-1]:
#                     return False
#             elif not flag and  not is_increasing:
#                 if nums[i] > nums[i-1]:
#                     return False
#         return True
        