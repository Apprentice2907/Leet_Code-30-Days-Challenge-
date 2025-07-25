'''You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

Example 1:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Explanation:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

Output: [null, 7, 7, 7, 8]

Explanation:

KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8
 

Constraints:

0 <= nums.length <= 104
1 <= k <= nums.length + 1
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.'''












# My logic but time limit exceeded

# class KthLargest(object):

#     def __init__(self, k, nums):
#         """
#         :type k: int
#         :type nums: List[int]
#         """
#         self.k = k
#         self.nums = nums

#         for i in range(len(self.nums)):
#             for j in range(i + 1, len(self.nums)):
#                 if self.nums[j] > self.nums[i]:
#                     self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        

#     def add(self, val):
#         """
#         :type val: int
#         :rtype: int
#         """
#         inserted = False
#         for i in range(len(self.nums)):
#             if val >= self.nums[i]:
#                 self.nums.insert(i, val)
#                 inserted = True
#                 break
#         if not inserted:
#             self.nums.append(val)

#         if len(self.nums) >= self.k:
#             return self.nums[self.k - 1]
#         else:
#             return None 
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)











# ChatGPT Heap Logic most efficient

# import heapq

# class KthLargest:
#     def __init__(self, k, nums):
#         self.k = k
#         self.heap = []

#         for num in nums:
#             self.add(num)

#     def add(self, val):
#         heapq.heappush(self.heap, val)

#         if len(self.heap) > self.k:
#             heapq.heappop(self.heap)

#         return self.heap[0]













# ChatGPT logic 

# class KthLargest:
#     def __init__(self, k, nums):
#         self.k = k
#         self.nums = sorted(nums, reverse=True)  

#     def add(self, val):
#         inserted = False
#         for i in range(len(self.nums)):
#             if val >= self.nums[i]:
#                 self.nums.insert(i, val)
#                 inserted = True
#                 break

#         if not inserted:
#             self.nums.append(val)

#         return self.nums[self.k - 1] 


