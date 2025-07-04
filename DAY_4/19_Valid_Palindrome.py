'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.'''





class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = ''.join(char.lower() for char in s if char.isalnum())

        return cleaned == cleaned[::-1]



'''class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s =  s.lower()
        i, j = 0, len(s)-1
        while i<j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    return False
                else:
                    i+=1
                    j-=1
            if s[i].isalnum() is False:
                i+=1
            if  s[j].isalnum() is False:
                j-=1
        return True
        '''