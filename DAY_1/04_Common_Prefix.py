'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):  # vertical loop over character indices
            char = strs[0][i]  # take the character from the first string
            for string in strs[1:]:  # horizontal loop over each string
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]  # return prefix up to mismatch
        return strs[0]  # all characters matched in the shortest string


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"])) 





# Space Complexity best output

# if not strs:
#             return ""
        
#         # Находим самую короткую строку в списке
#         shortest = min(strs, key=len)
        
#         for i, char in enumerate(shortest):
#             for s in strs:
#                 if s[i] != char:
#                     return shortest[:i]
        
#         return shortest