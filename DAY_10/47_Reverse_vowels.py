'''Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"
Output: "leotcede"'''






# My logic

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        chars = list(s)
        v = []
        idx = []

        i = 0
        for ch in s:
            if ch.lower() in vowels:
                v.append(ch)
                idx.append(i)
            i += 1

        v.reverse()

        for j in range(len(idx)):
            chars[idx[j]] = v[j]

        return ''.join(chars)
        





# Leetcode best solution

# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
    
#         left, right = 0, len(s) - 1
#         vowels = set("aeiouAEIOU")
#         word = list(s)

#         while left < right:
#             leftLetter = word[left]
#             rightLetter = word[right]
#             while left < right and leftLetter not in vowels:
#                 left += 1
#                 leftLetter = word[left]
#             while left < right and rightLetter not in vowels:
#                 right -= 1
#                 rightLetter = word[right]
#             word[left], word[right] = rightLetter, leftLetter
#             left += 1
#             right -= 1
#         return "".join(word)       






# Best ChatGPT solution

# class Solution(object):
#     def reverseVowels(self, s):
#         vowels = 'aeiouAEIOU'
#         chars = list(s)
#         left = 0
#         right = len(chars) - 1

#         while left < right:
#             # Move left pointer to the next vowel
#             while left < right and chars[left] not in vowels:
#                 left += 1
#             # Move right pointer to the previous vowel
#             while left < right and chars[right] not in vowels:
#                 right -= 1
#             # Swap the vowels
#             chars[left], chars[right] = chars[right], chars[left]
#             left += 1
#             right -= 1

#         return ''.join(chars)
