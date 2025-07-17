'''Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"'''









# My logic and simple using condition and loops 

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2 * k):
            if i + k > len(s):
                s[i:] = reversed(s[i:])
            elif i + 2 * k > len(s):
                s[i:i + k] = reversed(s[i:i + k])
            else:
                s[i:i + k] = reversed(s[i:i + k])
        return ''.join(s)
    










# Leet Code Best solution

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def reverse(s):
            return s[-1::-1]
        new_string = ''
        while True:
            if len(s) < k:
                return new_string + reverse(s)
            elif len(s) < 2*k:
                return new_string + reverse(s[:k]) + s[k:]
            else:
                new_string += reverse(s[:k]) + s[k:2*k]
                s = s[2*k:]