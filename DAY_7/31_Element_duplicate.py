'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 '''



#  my Logic but time complexity is O(n^2)

# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j] and abs(i - j) <= k:
#                     return True
#         return False
                



# Online and logical
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            
            # Keep the window size at most k
            if len(seen) > k:
                seen.remove(nums[i - k])
        
        return False





# Leetcode Best Solution

# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         d = {}
#         for idx, value in enumerate(nums):
#             if value in d and idx-d[value] <= k:
#                 return True
#             else:
#                 d[value] = idx
#         return False