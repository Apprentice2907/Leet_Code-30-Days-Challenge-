'''Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]'''







# My logic

class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        even_idx = 0
        odd_idx = 1

        for num in nums:
            if num % 2 == 0:
                res[even_idx] = num
                even_idx += 2
            else:
                res[odd_idx] = num
                odd_idx += 2

        return res
            






# Another code

# class Solution(object):
#     def sortArrayByParityII(self, nums):
        
#         even = [i for i in nums if i%2 == 0]
#         odd = [i for i in nums if i%2 != 0]

#         new_l = []

#         for i in range(len(even)):
#             new_l.append(even[i])
#             new_l.append(odd[i])

#         return new_l

#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
        