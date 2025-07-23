'''Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

 

Example 1:

Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.
Example 2:

Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.'''












# My logic simple and easy

class Solution(object):
    def shortestCompletingWord(self, lp, ws):
        lp = lp.lower()
        req = {}
        for c in lp:
            if c.isalpha():
                if c in req:
                    req[c] += 1
                else:
                    req[c] = 1

        res = None
        for w in ws:
            cnt = {}
            for ch in w.lower():
                if ch in req:
                    if ch in cnt:
                        cnt[ch] += 1
                    else:
                        cnt[ch] = 1
            valid = True
            for ch in req:
                if ch not in cnt or cnt[ch] < req[ch]:
                    valid = False
                    break
            if valid:
                if res is None or len(w) < len(res):
                    res = w
        return res

















# Leet code best solution

# class Solution(object):
#     def shortestCompletingWord(self, licensePlate, words):
#         """
#         :type licensePlate: str
#         :type words: List[str]
#         :rtype: str
#         """
#         l=[]
#         for i in licensePlate:
#             if i.isalpha():
#                 l.append(i.lower())
#         words.sort(key=len)
#         for i in words:
#             x=1
#             for j in l:
#                 if (j not in i) or (l.count(j)>i.count(j)):
#                     x=0
#                     break
#             if(x==1):
#                 return(i)