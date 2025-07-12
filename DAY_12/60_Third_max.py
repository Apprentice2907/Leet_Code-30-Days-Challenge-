'''Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.'''






# Simple and my logic using -3 index if available after sorting

class Solution(object):
    def thirdMax(self, nums):
        unique = list(set(nums))
        unique.sort()
        if len(unique) >= 3:
            return unique[-3]
        else:
            return unique[-1]










# Unique Logic ChatGPT

# class Solution(object):
#     def thirdMax(self, nums):
#         first = second = third = None

#         for x in nums:
#             if x == first or x == second or x == third:
#                 continue            # skip duplicates

#             if first is None or x > first:
#                 third, second, first = second, first, x
#             elif second is None or x > second:
#                 third, second = second, x
#             elif third is None or x > third:
#                 third = x

#         return third if third is not None else first






# import heapq

# class Solution(object):
#     def thirdMax(self, nums):
#         unique = set(nums)
#         if len(unique) < 3:
#             return max(unique)
#         return heapq.nlargest(3, unique)[-1]
