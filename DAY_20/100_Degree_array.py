'''Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.'''

















# My logic simple and easy to apply

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_index = {}
        freq = {}
        max_freq = 0
        min_length = 10000000000000000

        for i in range(len(nums)):
            num = nums[i]
            
            if num not in first_index:
                first_index[num] = i

            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            if freq[num] > max_freq:
                max_freq = freq[num]
                min_length = i - first_index[num] + 1
            elif freq[num] == max_freq:
                length = i - first_index[num] + 1
                if length < min_length:
                    min_length = length

        return min_length
            







# Leet Code Best Solution

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}
        # initialize 3 dictionaries

        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i; # save start index with our number as the key
            
            right[num] = i; # assign & update last index of the number spotted
            # count.get(num, 0) will return 0 if our num key is not found in the count dictionary
            count[num] = count.get(num, 0) + 1

        # now we have 3 dictionaries which can be queried with our num key
        # left which holds the first idx our number is spotted at in nums
        # right containing the last idx our number is spotted at in nums
        # count holding the number of times our number has been spotted

        min_range = len(nums) # maximum possible range value
        degree = max(count.values()) # count.values() returns a list of all of our counts, max finds the largest one in the list
        # go through all entires in our count dictionary and check their range if they match our max count
        for key in count:
            if count[key] == degree:
                min_range = min(min_range, right[key] - left[key] + 1)
                # find the minimum between our current min_range and the range calculated for the current key in our loop
        
        return min_range
            
        