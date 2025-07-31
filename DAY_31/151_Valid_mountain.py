'''Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true'''











# My logic and simple looping and conditional  

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False

        inc = False
        dec = False

        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                return False
            elif not dec and arr[i] > arr[i - 1]:
                inc = True
            elif inc and arr[i] < arr[i - 1]:
                dec = True
            else:
                return False

        return inc and dec
    










# Leetcode best solution 

# class Solution(object):
#     def validMountainArray(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: bool
#         """
#         n = len(arr)
#         if n < 3:
#             return False
#         i = 0
#     # Walk up
#         while i + 1 < n and arr[i] < arr[i + 1]:
#             i += 1
#     # Peak can't be first or last
#         if i == 0 or i == n - 1:
#             return False
#     # Walk down
#         while i + 1 < n and arr[i] > arr[i + 1]:
#             i += 1
#         return i == n - 1