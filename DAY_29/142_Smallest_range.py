'''You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

 

Example 1:

Input: nums = [1], k = 0
Output: 0
Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
Example 2:

Input: nums = [0,10], k = 2
Output: 6
Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
Example 3:

Input: nums = [1,3,6], k = 3
Output: 0
Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.'''












# my logic but chatGPT for understanding

class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min = nums[0]
        max = nums[0]

        for i in nums:
            if i < min:
                min = i
            if i > max:
                max = i

        diff = max - min - 2 * k

        if diff < 0:
            return 0
        else:
            return diff
        


# Leet code best solution

# class Solution(object):
#     def smallestRangeI(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         maxNum = max(nums)
#         minNum = min(nums)

#         if maxNum - minNum - 2*k <= 0:
#             return 0
#         return maxNum - minNum - 2*k