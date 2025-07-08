'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false'''








# Logiv=c using a dictionary to map characters to words and same with words to characters.

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, word in zip(pattern, words):
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                if word in word_to_char:
                    return False
                char_to_word[ch] = word
                word_to_char[word] = ch

        return True










# ChatGPT Use a single dictionary + set

# class Solution(object):
#     def wordPattern(self, pattern, s):
#         words = s.split()
#         if len(pattern) != len(words):
#             return False

#         mapping = {}
#         used_words = set()

#         for ch, word in zip(pattern, words):
#             if ch in mapping:
#                 if mapping[ch] != word:
#                     return False
#             else:
#                 if word in used_words:
#                     return False
#                 mapping[ch] = word
#                 used_words.add(word)

#         return True














# ChatGPT Use index mapping trick (clever, very short)

# class Solution(object):
#     def wordPattern(self, pattern, s):
#         words = s.split()
#         return len(pattern) == len(words) and \
#                [pattern.index(c) for c in pattern] == [words.index(w) for w in words]
