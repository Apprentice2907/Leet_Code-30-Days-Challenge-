'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).'''




class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0 

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i] 
                count += 1
            else:
                nums[i] = '_'  

        for i in range(count, len(nums)):
            nums[i] = '_'

        return count



# my idea 
# making new empty list and then appending elements or _ if not found but the rules says to not create a new list
        

nums = [3, 2, 2, 3]
val = 3
solution = Solution()
k = solution.removeElement(nums, val)
print("k:", k)
print("Modified nums:", nums)



# buggy output as the output comes [2,2,2,"_"] instead of [2,2,_,_]

# for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[count] = nums[i]
#                 if count != i:
#                     nums[i] = '_'  # Mark the old position (which had val)
#                 count += 1
#             else:
#                 nums[i] = '_'  # Mark the removed value

#         return count