'''Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.'''









# My logic but not optimal

# class Solution(object):
#     def findLengthOfLCIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         ans = 1 
#         for i in range(n):
#             count = 1
#             for j in range(i + 1, n):
#                 if nums[j] > nums[j - 1]:
#                     count += 1
#                     ans = max(ans, count)
#                 else:
#                     break
#         return ans






# Leet code best solution

# class Solution(object):
#     def findLengthOfLCIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0

#         count = 1
#         max_count = 1

#         for i in range(1, len(nums)):
#             if nums[i] > nums[i - 1]:
#                 count += 1
#                 max_count = max(max_count, count)
#             else:
#                 count = 1  # reset count when the sequence breaks

#         return max_count

