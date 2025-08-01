'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]'''









# My logic 

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
        









# Unique Logic

# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         #[-3, -2, -1, 0, 1, 2, 3]
#         left = 0
#         n = len(nums)
#         right = n-1
#         answer = [0] * n

#         for i in range(n-1, -1, -1):
#             if abs(nums[left]) < abs(nums[right]):
#                 num = nums[right]
#                 right -= 1
#             else:
#                 # abs(nums[left]) > abs(nums[right])
#                 num = nums[left]
#                 left += 1
#             answer[i] = num * num

#         return answer
        