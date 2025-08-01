'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''



class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

sol = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))



# Best answer

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         array = {}  # Dictionary to store number to index mapping
#         for i in range(len(nums)):
#             next_num=target-nums[i]

#             if next_num in array:
#                 return [array[next_num] , i]

#             array[nums[i]]= i
        
#         return []
