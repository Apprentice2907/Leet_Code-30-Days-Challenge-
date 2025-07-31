'''In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).'''










# My logic but chatGPT coded

class Solution(object):
    def isAlienSorted(self, words, order):
        od = {}
        index = 0
        for ch in order:
            od[ch] = index
            index += 1

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if word1.startswith(word2) and len(word1) > len(word2):
                return False

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if od[word1[j]] > od[word2[j]]:
                        return False
                    break

        return True









# Another logic in Leetcode

# class Solution(object):
#     def isAlienSorted(self, words, order):
#         weight={}
#         w=0
#         for i in order:
#             weight[i]=w
#             w+=1

#         for j in range(len(words) - 1):
#             word1 = words[j]
#             word2 = words[j + 1]
#             esc=False
#             for char in range(min(len(word1), len(word2))):
#                 if word1[char]!=word2[char]:
#                     if weight[word1[char]]<weight[word2[char]]:
#                         esc=True
#                         break
#                     elif weight[word1[char]]>weight[word2[char]]:
#                         return False
#             if not esc and len(word1)>len(word2):
#                 return False 

                
#         return True       

