'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''





#  Best answer
class Solution(object):
    def majorityElement(self, nums):
        count , res = 0 , 0
        for n in nums:
            if count == 0:
                res = n
            count+=(1 if res ==n else -1)
        return res



#  personal but not time effective

# class Solution(object):
#     def majorityElement(self, nums):
#         n = len(nums) // 2
#         for i in range(len(nums)):
#             cur = 1
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     cur += 1
#             if cur > n:
#                 return nums[i]
#         return None