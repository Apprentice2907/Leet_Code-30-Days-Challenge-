'''We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.'''













# My logic 
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) == 1:
            return 0

        counts = {}
        for number in nums:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1

        longest = 0
        for current in counts:
            if current + 1 in counts:
                total = counts[current] + counts[current + 1]
                if total > longest:
                    longest = total

        return longest
    













# Leet Code Best solution

# from collections import Counter
# class Solution(object):
#     def findLHS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         '''
#         max_len = 0
#         for i in range(len(nums)):
#             cnt = 0
#             for j in range(len(nums)):
#                 if nums[j] == nums[i] or nums[j] == nums[i] + 1:
#                     cnt += 1
#             if cnt > max_len and nums.count(nums[i] + 1) > 0:
#                 max_len = cnt
#         return max_len 
#         '''

#         # Hashmap
#         cnt = Counter(nums)
#         max_len = 0

#         for num in cnt:
#             if num + 1 in cnt:
#                 max_len = max(max_len, cnt[num] + cnt[num + 1])

#         return max_len

        
        