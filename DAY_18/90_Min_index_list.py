'''Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

 

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
Example 3:

Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".'''














# My logic

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        least = 2000
        result = []

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum = i + j
                    if index_sum < least:
                        result = [list1[i]]
                        least = index_sum
                    elif index_sum == least:
                        result.append(list1[i])

        return result
    








# Leet Code Best solution

# class Solution(object):
#     def findRestaurant(self, list1, list2):
#         index_map = {s: i for i, s in enumerate(list1)}
#         min_sum = float('inf')
#         result = []

#         for j, s in enumerate(list2):
#             if s in index_map:
#                 i = index_map[s]
#                 index_sum = i + j
#                 if index_sum < min_sum:
#                     min_sum = index_sum
#                     result = [s]
#                 elif index_sum == min_sum:
#                     result.append(s)
        
#         return result