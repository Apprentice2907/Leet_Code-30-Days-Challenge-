'''You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000'''








# My code but error not passed the test case
# ChatGPT gives error while coding this 

# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         if len(nums) < k:
#             return 0

#         total = sum(nums[:k])
#         avg = total / k

#         for i in range(1, len(nums) - k + 1):
#             total = sum(nums[i:i+k])
#             curr_avg = total / k
#             if curr_avg > avg:
#                 avg = curr_avg

#         return avg











# Leet code solution passed

# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         s = sum(nums[:k])
#         m = s
#         for i in range(k, len(nums)):
#             s += nums[i] - nums[i - k]
#             if s > m:
#                 m = s
#         return m / float(k)
    







# Third logic combining both codes above 
class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums) < k:
            return 0

        total = sum(nums[:k])
        max_sum = total

        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]
            if total > max_sum:
                max_sum = total

        return max_sum / float(k)
