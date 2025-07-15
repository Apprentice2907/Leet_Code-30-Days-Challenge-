'''The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.'''












# My logic 

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []

        for x in nums1:
            found = False
            greater = -1
            for i in range(len(nums2)):
                if nums2[i] == x:
                    found = True
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > x:
                            greater = nums2[j]
                            break
                    break
            result.append(greater)

        return result
    







# Leet Code Best Solution

# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
#         stack = []
#         hm = {}

#         for n in nums2:
#             while stack and n > stack[-1]:
#                 old_top = stack.pop()
#                 hm[old_top] = n
#             stack.append(n)

#         result = []
#         for n in nums1:
#             result.append(hm.get(n, -1))

#         return result