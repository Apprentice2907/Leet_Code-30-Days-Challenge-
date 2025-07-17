'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 '''






# My logic

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = []

        for word in words:
            reversed_word = ''
            for ch in reversed(word):
                reversed_word += ch
            result.append(reversed_word)

        return ' '.join(result)
    








# Best LeetCode solution

class Solution(object):
    def reverseWords(self, s):
        return " ".join([w[::-1] for w in s.split(" ")])