'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 '''





# Set Logic 

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = set()
        set2 = set(nums2)

        for i in nums1:
            if i in set2:
                res.add(i)

        return list(res)











# ChatGPT best solution

# def intersection_sorted(nums1, nums2):
#     nums1.sort()
#     nums2.sort()
    
#     i, j = 0, 0
#     res = []

#     while i < len(nums1) and j < len(nums2):
#         a, b = nums1[i], nums2[j]

#         if a == b:
#             # Add only if it's not already in result (keeps uniqueness)
#             if not res or res[-1] != a:
#                 res.append(a)
#             i += 1
#             j += 1
#         elif a < b:
#             i += 1
#         else:
#             j += 1

#     return res
