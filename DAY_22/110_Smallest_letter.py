'''You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.'''




# Simple and easy my logic

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for char in letters:
            if char > target:
                return char
        return letters[0]
    




# Another Leet Code Logic

# class Solution(object):
#     def nextGreatestLetter(self, letters, target):
#         """
#         :type letters: List[str]
#         :type target: str
#         :rtype: str
#         """
#         left, right = 0, len(letters) - 1

#         while left <= right:
#             mid = (left + right) // 2
#             if letters[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return letters[left] if left < len(letters) else letters[0]