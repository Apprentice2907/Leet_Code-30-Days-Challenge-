'''iven a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 '''







# my logic using odd as center and then appending at 0 and -1 index

class Solution(object):
    def longestPalindrome(self, s):
        from collections import Counter

        count = Counter(s)
        left = []      
        center = ''    
        right = []     

        for char in count:
            freq = count[char]

            if freq % 2 == 0:
                left.append(char * (freq // 2))
                right.insert(0, char * (freq // 2))  
            else:
                if center == '':
                    center = char  
                left.append(char * (freq // 2))
                right.insert(0, char * (freq // 2))

        palindrome = ''.join(left) + center + ''.join(right)
        return len(palindrome)









# using the above logic only

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         from collections import Counter
#         count = Counter(s)
#         length = 0
#         odd_used = False 
#         for char, freq in count.items():
#             if freq % 2 == 0:
#                 length += freq 
#             else:
#                 length += freq - 1  
#                 odd_used = True     
#         if odd_used:
#             length += 1
#         return length








# Leet code best solution

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         from collections import Counter
#         count = Counter(s)
#         length = 0
#         odd_found = False
#         for v in count.values():
#             length += v // 2 * 2
#             if v % 2 == 1:
#                 odd_found = True
#         if odd_found:
#             length += 1
#         return length