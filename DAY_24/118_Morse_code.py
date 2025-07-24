'''International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

 

Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
Example 2:

Input: words = ["a"]
Output: 1'''











# My logic simple for me 

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        letters = "abcdefghijklmnopqrstuvwxyz"
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]

        mapping = {}
        for i in range(len(letters)):
            mapping[letters[i]] = codes[i]

        result = []
        for word in words:
            code = ""
            for ch in word:
                code += mapping[ch]
            result.append(code)

        unique = []
        for val in result:
            if val not in unique:
                unique.append(val)

        return len(unique)









# Best leet code solution

# class Solution(object):
#     def uniqueMorseRepresentations(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """
        
#         morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
#         return len({''.join(morse[ord(c)-97] for c in w) for w in words})

#         codes = set()

#         for word in words:
#             code = ""
#             for char in word:
#                 code += morse[ord(char)-97]
#             codes.add(code)
        
#         return len(codes)