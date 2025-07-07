'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 '''










class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0

        for j in range(1, len(nums) + 1):
            if j == len(nums) or nums[j] != nums[j - 1] + 1:
                start = nums[i]
                end = nums[j - 1]
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                i = j  # move i to start of next range

        return res




#  All logics 

# 1 . Your Original Logic – Two Loops (Brute Force Style)
# Description:
# You loop through the array using two nested loops:
# Outer loop tracks the start of the range.
# Inner loop checks if the next number is consecutive (nums[j] == nums[j-1] + 1).
# When a non-consecutive number is found, you format and add the range ("a" or "a->b") to the result.
# Then start the next range from the next number.

# Pros:
# Easy to understand conceptually.
# Good for learning how ranges form.
# Cons:
# Inefficient (O(n²)) for large arrays.



# 2. Improved Using for Loop and Single Pointer
# Description:
# Use a single pointer i to mark the start of a range, and iterate j from 1 to n.
# At each step:
# If nums[j] is not consecutive (nums[j] != nums[j-1] + 1), that means the current range ends at j-1.
# Format the range from nums[i] to nums[j-1].
# Move i to j to start the next range.

# Pros:
# Efficient (O(n))
# Cleaner than nested loops
# Easy to implement with for loop

# 3. Start-End Tracker (Using while Loop)
# Description:
# Loop over the array with index i.
# For each number:
# Mark it as the start of a new range.
# Keep moving i forward while the next number is consecutive.
# When the sequence breaks, mark the end and add "a" or "a->b" to the result.
# Repeat with the next element.

# Pros:
# Very clean and readable.
# Only one loop → efficient.
# Mimics how we naturally group ranges.

# 4. Functional / Sliding Window / Set-based (Used in other problems)
# Note: Not directly needed for summary ranges, but useful in similar problems like “contains nearby duplicate”.
# Keep a sliding window or set of k previous values.
# Efficient checking of recent items.






# ChatGPT using while loop

# class Solution(object):
#     def summaryRanges(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[str]
#         """
#         res = []
#         i = 0
#         n = len(nums)

#         while i < n:
#             start = nums[i]
#             j = i
#             # Loop to find the end of consecutive sequence
#             while j + 1 < n and nums[j + 1] == nums[j] + 1:
#                 j += 1

#             end = nums[j]
#             if start == end:
#                 res.append(str(start))
#             else:
#                 res.append(str(start) + "->" + str(end))
            
#             # Move i to the next new range
#             i = j + 1
        
#         return res
