'''Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Note that words can not contain punctuation symbols.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.'''














# My logic simple but chatGPT coded

# import string

# class Solution(object):
#     def mostCommonWord(self, paragraph, banned):
#         for p in string.punctuation:
#             paragraph = paragraph.replace(p, " ")
#         words = paragraph.lower().split()
        
#         for ban in banned:
#             while ban in words:
#                 words.remove(ban)
        
#         max_word = ""
#         max_count = 0
        
#         for word in set(words):
#             count = words.count(word)
#             if count > max_count:
#                 max_count = count
#                 max_word = word
        
#         return max_word




# SImple and short code of above code 

import string

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for p in string.punctuation:
            paragraph = paragraph.replace(p, ' ')
        words = paragraph.lower().split()
        for b in banned:
            while b in words:
                words.remove(b)
        return max(set(words), key=words.count)













# Leet code best solution

# from collections import Counter
# import re
# class Solution(object):
#     def mostCommonWord(self, paragraph, banned):

#         normalized_str = re.sub(r'[^\w]', ' ', paragraph).lower()
#         words = normalized_str.split()
        
    
#         banned_set = set(banned)
        
#         word_counts = Counter(word for word in words if word not in banned_set)
        
        
#         return word_counts.most_common(1)[0][0]
               
        

        