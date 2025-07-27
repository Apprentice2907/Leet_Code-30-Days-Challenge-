'''A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 '''









# My logic 

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words1 = s1.split()
        words2 = s2.split()
        count = {}

        for word in words1:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        for word in words2:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        result = []
        for word in count:
            if count[word] == 1:
                result.append(word)

        return result
    







# Leetcode best solution

# class Solution(object):
#     def uncommonFromSentences(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: List[str]
#         """
#         s=s1+" "+s2
#         s=s.split()
#         c=Counter(s)
#         print(c)
#         li=[]
#         for i in c:
#             if c[i]==1:
#                 li.append(i)
#         return li
        