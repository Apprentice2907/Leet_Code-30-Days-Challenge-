'''You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat Latin.

 

Example 1:

Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"'''








# Best and my logic using conditional statement

class Solution:
    def toGoatLatin(self, sentence):
        vowels = 'aeiouAEIOU'
        words = sentence.split()
        result = []

        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word = word + "a" * (i + 1)
            result.append(word)

        return " ".join(result)










# Another logic but not effiecnt

# class Solution(object):
#     def toGoatLatin(self, sentence):
#         """
#         :type sentence: str
#         :rtype: str
#         """
#         start_word=True
#         vowels= set(['a', 'e', 'i', 'o', 'u'])
#         word_count =1
#         result=[]
#         to_add=""
#         for c in sentence:
#             if c==" ":
#                 start_word=True
#                 result.append(to_add)
#                 for _ in range(word_count):
#                     result.append('a')
#                 word_count+=1
#                 to_add=""
#                 result.append(c)
#                 continue
#             if start_word:
#                 start_word=False
#                 if c.lower() in vowels:
#                     to_add="ma"
#                 else:
#                     to_add=c+"ma"
#                     continue
#             result.append(c)
#         result.append(to_add)
#         for _ in range(word_count):
#             result.append('a')
#         return "".join(result)