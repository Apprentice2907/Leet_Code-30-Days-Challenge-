'''Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0'''








# My logic using loop and taking an element at a time 

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        return -1







# My logic similar to binary search method but doesnt pass the test cases

# class Solution(object):
#     def pivotIndex(self, nums):
#         left = 0
#         right = len(nums) - 1
        
#         while left <= right:
#             mid = (left + right) // 2
#             left_sum = sum(nums[:mid])
#             right_sum = sum(nums[mid+1:])
            
#             if left_sum == right_sum:
#                 return mid
#             elif left_sum < right_sum:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         # Check remaining possible pivots just in case
#         for i in range(len(nums)):
#             if sum(nums[:i]) == sum(nums[i+1:]):
#                 return i
        
#         return -1









# Best solution time complexity O(n) and space complexity O(1)

# class Solution(object):
#     def pivotIndex(self, nums):
#         total = sum(nums)
#         left_sum = 0
#         for i, num in enumerate(nums):
#             if left_sum == total - left_sum - num:
#                 return i
#             left_sum += num
#         return -1







# Leet code best solution

# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
# # Time Complexity : O(n)
# # Space Complexity : O(1)
# class Solution(object):
#     def pivotIndex(self, nums):    

#         leftSum, rightSum = 0, sum(nums)
    
#         for idx, ele in enumerate(nums):

#             rightSum -= ele

#             if leftSum == rightSum:
#                 return idx     
#             leftSum += ele
#         return -1       
        