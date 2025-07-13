'''Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]'''



# My logic but time limit exceeded

# class Solution:
#     def findDisappearedNumbers(self, nums):
#         missing = []
#         for i in range(1, len(nums) + 1):  
#             if i not in nums:
#                 missing.append(i)
#         return missing



# Time limit same logic with code optimization , leet code best solution is same as this only

class Solution:
    def findDisappearedNumbers(self, nums):
        missing = []
        num_set = set(nums) 

        for i in range(1, len(nums) + 1):  
            if i not in num_set:          
                missing.append(i)

        return missing





# Unique Logic

# class Solution:
#     def findDisappearedNumbers(self, nums):
#         for num in nums:
#             index = abs(num) - 1
#             if nums[index] > 0:
#                 nums[index] = -nums[index]
        
        
#         missing = []
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 missing.append(i + 1)

#         return missing



        
        