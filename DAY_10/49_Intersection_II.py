'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.'''






# My logic 

def intersect(nums1, nums2):
    copy_nums2 = nums2[:]      
    result = []

    for num in nums1:         
        if num in copy_nums2:  
            result.append(num)       
            copy_nums2.remove(num)    

    return result








# Leetcode Best solution
# class Solution(object):
#     def intersect(self, nums1, nums2):
#         from collections import Counter
#         counts = Counter(nums1)
#         res = []
#         for n in nums2:
#             if counts[n] > 0:
#                 res.append(n)
#                 counts[n] -= 1
#         return res
        











#  Frequency‑map (hash‑table) — O(n + m) time, O(min(n,m)) space
# Count how many times each value appears in the smaller array,
# then walk through the other array and consume those counts.



# def intersect_hash(nums1, nums2):
#     # Always count the shorter list to save space
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1
#     freq = {}                          # value -> remaining count
#     for x in nums1:                    # build the counts
#         freq[x] = freq.get(x, 0) + 1  
#     res = []
#     for x in nums2:                    # consume counts
#         if freq.get(x, 0):
#             res.append(x)
#             freq[x] -= 1
    
#     return res










# 2. Sort + Two Pointers — O(n log n + m log m) time, O(1) extra space


# def intersect_sorted(nums1, nums2):
#     nums1.sort()
#     nums2.sort()
#     i = j = 0
#     res = []

#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] == nums2[j]:
#             res.append(nums1[i])
#             i += 1
#             j += 1
#         elif nums1[i] < nums2[j]:
#             i += 1
#         else:
#             j += 1
#     return res
